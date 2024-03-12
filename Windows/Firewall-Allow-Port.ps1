# Windows PowerShell Command-Line Firewall Allow Port 80, 443, 3000, 5000, 8000-8080
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP" -Direction Inbound -Protocol TCP -LocalPort 80, 443, 3000, 5000, 8000-8080 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP" -Direction Outbound -Protocol TCP -LocalPort 80, 443, 3000, 5000, 8000-8080 -Action Allow

# 80
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-80" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-80" -Direction Outbound -Protocol TCP -LocalPort 80 -Action Allow

# 443
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-443" -Direction Inbound -Protocol TCP -LocalPort 443 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-443" -Direction Outbound -Protocol TCP -LocalPort 443 -Action Allow

# 3000
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-3000" -Direction Inbound -Protocol TCP -LocalPort 3000 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-3000" -Direction Outbound -Protocol TCP -LocalPort 3000 -Action Allow

# 8000
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-8000" -Direction Inbound -Protocol TCP -LocalPort 8000 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-8000" -Direction Outbound -Protocol TCP -LocalPort 8000 -Action Allow

# 8080
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-8080" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow
New-NetFirewallRule -DisplayName "DEVELOP" -Description "DEVELOP-8080" -Direction Outbound -Protocol TCP -LocalPort 8080 -Action Allow

# 15100, 15101 
New-NetFirewallRule -DisplayName "Mouse Without Border" -Description "Mouse Without Border" -Direction Inbound -Protocol TCP -LocalPort 15100, 15101 -Action Allow
New-NetFirewallRule -DisplayName "Mouse Without Border" -Description "Mouse Without Border" -Direction Outbound -Protocol TCP -LocalPort 15100, 15101 -Action Allow

#