# Completely remove Visual Studio Code from Windows
# This script removes:
# - Program files
# - User settings
# - Extensions
# - Cache and state folders

Write-Host "Stopping VS Code if running..."
Get-Process "Code" -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Host "Uninstalling Visual Studio Code (if installed)..."
$uninstallKeys = @(
    "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall",
    "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall",
    "HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
)

foreach ($key in $uninstallKeys) {
    Get-ChildItem $key -ErrorAction SilentlyContinue |
        Where-Object { $_.GetValue("DisplayName") -like "Visual Studio Code*" } |
        ForEach-Object {
            $uninstallString = $_.GetValue("UninstallString")
            if ($uninstallString) {
                Write-Host "Running uninstaller..."
                Start-Process -FilePath $uninstallString -ArgumentList "/VERYSILENT" -Wait
            }
        }
}

Write-Host "Removing leftover folders..."

$paths = @(
    "$env:LOCALAPPDATA\Programs\Microsoft VS Code",
    "$env:LOCALAPPDATA\Programs\Microsoft VS Code Insiders",
    "$env:APPDATA\Code",
    "$env:LOCALAPPDATA\Code",
    "$env:USERPROFILE\.vscode"
)

foreach ($path in $paths) {
    if (Test-Path $path) {
        Write-Host "Deleting $path"
        Remove-Item -Recurse -Force $path
    }
}

Write-Host "VS Code has been fully removed."