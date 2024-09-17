# Xóa tất cả các Inbound Rules có tên chứa "Python"
Get-NetFirewallRule -DisplayName *Python* -Direction Inbound | Remove-NetFirewallRule

# Xóa tất cả các Outbound Rules có tên chứa "Python"
Get-NetFirewallRule -DisplayName *Python* -Direction Outbound | Remove-NetFirewallRule
