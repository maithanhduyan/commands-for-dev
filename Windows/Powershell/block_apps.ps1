# Chặn Python qua TCP và UDP cả Inbound và Outbound
New-NetFirewallRule -DisplayName "Block Python Inbound TCP" -Program "C:\odoo\python\python.exe" -Action Block -Direction Inbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block Python Inbound UDP" -Program "C:\odoo\python\python.exe" -Action Block -Direction Inbound -Protocol UDP
New-NetFirewallRule -DisplayName "Block Python Outbound TCP" -Program "C:\odoo\python\python.exe" -Action Block -Direction Outbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block Python Outbound UDP" -Program "C:\odoo\python\python.exe" -Action Block -Direction Outbound -Protocol UDP

# Chặn Postman qua TCP và UDP cả Inbound và Outbound
New-NetFirewallRule -DisplayName "Block Postman Inbound TCP" -Program "C:\path\to\postman.exe" -Action Block -Direction Inbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block Postman Inbound UDP" -Program "C:\path\to\postman.exe" -Action Block -Direction Inbound -Protocol UDP
New-NetFirewallRule -DisplayName "Block Postman Outbound TCP" -Program "C:\path\to\postman.exe" -Action Block -Direction Outbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block Postman Outbound UDP" -Program "C:\path\to\postman.exe" -Action Block -Direction Outbound -Protocol UDP

# Chặn TeamViewer qua TCP và UDP cả Inbound và Outbound
New-NetFirewallRule -DisplayName "Block TeamViewer Inbound TCP" -Program "C:\Program Files\TeamViewer\TeamViewer.exe" -Action Block -Direction Inbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block TeamViewer Inbound UDP" -Program "C:\Program Files\TeamViewer\TeamViewer.exe" -Action Block -Direction Inbound -Protocol UDP
New-NetFirewallRule -DisplayName "Block TeamViewer Outbound TCP" -Program "C:\Program Files\TeamViewer\TeamViewer.exe" -Action Block -Direction Outbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block TeamViewer Outbound UDP" -Program "C:\Program Files\TeamViewer\TeamViewer.exe" -Action Block -Direction Outbound -Protocol UDP

# Chặn TeamViewer Service qua TCP và UDP cả Inbound và Outbound
New-NetFirewallRule -DisplayName "Block TeamViewer Service Inbound TCP" -Program "C:\Program Files\TeamViewer\TeamViewer_Service.exe" -Action Block -Direction Inbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block TeamViewer Service Inbound UDP" -Program "C:\Program Files\TeamViewer\TeamViewer_Service.exe" -Action Block -Direction Inbound -Protocol UDP
New-NetFirewallRule -DisplayName "Block TeamViewer Service Outbound TCP" -Program "C:\Program Files\TeamViewer\TeamViewer_Service.exe" -Action Block -Direction Outbound -Protocol TCP
New-NetFirewallRule -DisplayName "Block TeamViewer Service Outbound UDP" -Program "C:\Program Files\TeamViewer\TeamViewer_Service.exe" -Action Block -Direction Outbound -Protocol UDP
