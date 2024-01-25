# Windows PowerShell Command-Line Firewall Allow Port  3000, 5000, 8000-8080
New-NetFirewallRule -DisplayName "DEVELOP" -Direction Inbound -Protocol TCP -LocalPort 3000, 5000, 8000-8080 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Direction Outbound -Protocol TCP -LocalPort 3000, 5000, 8000-8080 -Action Allow
