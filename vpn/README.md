# VPN
## Introduction
<p>The purpose of this project is <strong>to connect 2 private network using VPN via Public Network</strong>. Private network is not routed in Public Network, to connect the private networks VPN is needed. The VPN will be configured using python from NetworkAutomation PC.</p>
<p>STEP : </p>
<ol>
<li>R2 must be connected to R1 and R3</li>
<li>R3 must be connected to R1 and R2</li>
<li>R1 is a representation of Public Network Router that does not route to any private networks</li>
<li>R2 is configured with VPN to connect to R3 private networks</li>
<li>R3 is configured with VPN to connect to R2 private networks</li>
<li>Check the connection between private networks</li>
<li>Check the packet using wireshark, it must be encapsulated using Security Protocol (IPSec)</li>
</ol>
<p>Set Up the topology like this below : </p>
<img src="vpn_1.png">
<p>Initial Configuration : </p>
<img src="vpn_table.PNG">
<p>Router R2 Configuration : </p>
<img src="vpn_r2.png">
<p>Router R3 Configuration : </p>
<img src="vpn_r3.png">
<p>Check connection between private networks : </p>
<img src="vpn_ping.png">
<img src="vpn_telnet.png">
<p>Check the packet using wireshark, it should be encapsulated with Security Protocols like below : </p>
<img src="vpn_wireshark.png">