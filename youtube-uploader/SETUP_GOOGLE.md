# One-time Google setup (about 10 minutes)

You do this once. After it, uploads run from your laptop with one command and cost **no Grok Bot usage**.

## 1. Create a Google Cloud project
1. Open https://console.cloud.google.com/ and sign in with the Google account that owns both channels.
2. Top bar → project picker → **New project** → name it `waqar-youtube-uploader` → **Create**. Make sure it is selected.

## 2. Turn on the YouTube Data API v3
1. Open https://console.cloud.google.com/apis/library/youtube.googleapis.com
2. Click **Enable**.

## 3. OAuth consent screen ("Google Auth Platform")
1. Open https://console.cloud.google.com/auth/overview → **Get started**.
2. App name `Waqar Uploader`, support email = your Gmail → **Next**.
3. Audience: **External** → **Next**. Contact email: your Gmail → **Finish/Create**.
4. **Audience** page → **Test users** → **Add users** → your Gmail → **Save**.
5. (Optional) **Data access** → Add scopes `.../auth/youtube.upload`, `.../auth/youtube`, `.../auth/youtube.force-ssl`. The script asks for them anyway.

> **Testing mode = sign-in expires every 7 days.** Google gives apps in "Testing" a refresh token that lasts
> 7 days ([Google OAuth docs](https://developers.google.com/identity/protocols/oauth2#expiration)). When it
> expires the script simply opens the sign-in page again. To stop that, go to **Audience → Publish app → In
> production**. You don't need Google verification for your own use: you'll just see an "unverified app" warning
> at sign-in (click **Advanced → Go to Waqar Uploader (unsafe)**) and the token then stays valid.

## 4. Create the Desktop OAuth client
1. https://console.cloud.google.com/auth/clients → **Create client**.
2. Application type **Desktop app**, name `laptop` → **Create**.

## 5. Download client_secret.json
1. In the dialog (or the client's row) click **Download JSON**.
2. Rename it to `client_secret.json` and put it in `youtube-uploader\secrets\` (create the folder).
3. **Never commit it.** `.gitignore` already blocks `secrets/`, `config.yaml`, tokens and `uploaded.json`.

## 6. Sign in once per channel
```bat
run.bat auth --channel happy
run.bat auth --channel build
```
The browser opens → choose your Google account → **choose the channel** (Happy Learners ICSE or
Waqar Shaikh Builds; both are brand accounts under the same login) → **Allow**. The script prints
`Profile 'happy' -> channel 'Happy Learners ICSE' id UC...`. Copy that `channel_id` into `config.yaml`;
uploads then refuse to run if the token ever points at the wrong channel.

In WSL, if no browser opens, copy the printed URL into Windows Chrome; the redirect to `localhost` works
from WSL 2. (Use `--no-browser` to only print the URL.)

## 7. Custom thumbnails
Thumbnail upload needs a **verified channel** (phone verification at https://www.youtube.com/verify) - both
channels already use custom thumbnails, so this should already be fine.

---

## Do uploads become public / scheduled without a Google "audit"?  (checked 31 Oct 2026)

**Short answer: yes, today. No audit is needed for public or scheduled uploads. The script still handles the old rule if it ever comes back.**

* **Old rule (28 July 2020):** "All videos uploaded via the `videos.insert` endpoint from unverified API projects
  created after 28 July 2020 will be restricted to private viewing mode" until the project passed an audit
  ([Revision history, July 28 2020](https://developers.google.com/youtube/v3/revision_history)).
* **Current rule (2026):** Google has lifted that restriction. In the YouTube API issue tracker, Google staff said:
  *"Videos uploaded from unverified API projects created after July 28, 2020, are no longer restricted to private
  viewing mode... An unaudited API project can successfully schedule a private video for public release using
  status.publishAt, and YouTube will honor that scheduled release... An API compliance audit is no longer
  required specifically to bypass the private-viewing restriction"*
  ([issue 572863050](https://issuetracker.google.com/issues/572863050),
  [issue 572902667](https://issuetracker.google.com/issues/572902667)).
  The `videos.insert` reference page has been updated to match, but the revision history page and the
  Help Center article still show the old text, which Google says it will fix.
* **When you still need the audit form:** only to get **more quota** than the default, or if YouTube asks for a re-audit.
  Form: **YouTube API Services - Audit and Quota Extension Form**, https://support.google.com/youtube/contact/yt_api_form
  (guide: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits). You need a privacy
  policy URL and your project number. Expect a reply in days to weeks.
* **Fallback if a video ever comes out "Locked (private)":** the script checks every upload and prints
  `LOCKED PRIVATE` (also shown by `status`). Either (a) set `upload: mode: private` in `config.yaml` so the script uploads everything
  private (thumbnail, captions and playlist are all still done), then in **YouTube Studio → Content → video → Visibility → Schedule**
  pick the date (one click per video), or (b) ask Grok Bot to flip the visibility, or (c) submit the audit form above.

### Quota (default 10,000 units / project / day, resets at midnight Pacific = 12:30 PM IST)
| call | units |
|---|---|
| videos.insert (long or Short) | 1,600 |
| captions.insert | 400 |
| thumbnails.set | 50 |
| playlistItems.insert | 50 |
| list calls | 1 |

One lesson (long + Short + thumbnail + captions + playlist) costs about **3,700 units**, so you can do **2 lessons a day**
(e.g. one per channel). Since June 2026 Google is moving `videos.insert` into its own bucket (100 calls/day)
([revision history, June 1 2026](https://developers.google.com/youtube/v3/revision_history)). The script still
counts it against the 10,000 to be safe, so if anything it under-estimates what you can do. To allow more, raise `quota: daily_units`.

### Made for kids and scheduling, as the script sets them
* `status.selfDeclaredMadeForKids: true` for Happy Learners. YouTube then turns off comments, cards, end screens and notifications (that's YouTube's rule, not the script's).
* Scheduling = `privacyStatus: private` + `publishAt` (UTC). YouTube makes it public at that minute. The time
  must be in the future, and the video must never have been public before.
* `--now` uploads straight to public.
