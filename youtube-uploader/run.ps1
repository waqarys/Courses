# Usage:  .\run.ps1 upload "C:\path\02_Plants" --channel happy
#         .\run.ps1 queue --channel happy -Log      (writes logs\queue_YYYYMMDD.log)
param([switch]$Log, [Parameter(ValueFromRemainingArguments = $true)] $Rest)
Set-Location $PSScriptRoot
if (-not (Test-Path .venv\Scripts\python.exe)) {
  Write-Host "Creating Python environment..."
  py -3 -m venv .venv
  .\.venv\Scripts\python.exe -m pip install --upgrade pip
  .\.venv\Scripts\python.exe -m pip install -r requirements.txt
}
New-Item -ItemType Directory -Force logs | Out-Null
$env:PYTHONIOENCODING = "utf-8"
if ($Log) {
  $f = "logs\$($Rest[0])_$(Get-Date -Format yyyyMMdd_HHmm).log"
  & .\.venv\Scripts\python.exe yt_upload.py @Rest *>&1 | Tee-Object -FilePath $f
} else {
  & .\.venv\Scripts\python.exe yt_upload.py @Rest
}
exit $LASTEXITCODE
