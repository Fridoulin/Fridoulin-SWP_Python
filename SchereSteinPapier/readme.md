</head>
<body lang="de-AT" link="#0563c1" vlink="#954f72" dir="ltr"><p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f"><font size="6" style="font-size: 24pt"><h1>Rock,
Paper, Scissors, Spock, Lizard</h1></font></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f"><font size="3" style="font-size: 12pt"><h3>Was
macht das Programm?</h3></font></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f">In diesem Programm kann man Schere, Stein,
Papier, Spock, Echse wobei Spock und Echse einfach zwei weitere
Symbole sind. Der Spieler spielt gegen den Computer und die Wahl des
Spielers wird in einer Datenbank gespeichert.</font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f"><font size="3" style="font-size: 12pt"><h3>Wie
funktioniert das Programm?</h3></font></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f">Das Programm fragt als erstes den Spieler,
welches Symbol er wählt, danach entscheidet der Computer mittel
random welches Symbol er nimmt. Die Wahl des Spielers wird nach jedem
Runde in einer Datenbank abgespeichert und nach der Runde wird die
Anzahl, wie oft welches Symbol gewählt wurde ausgegeben. Nach jeder
Runde sendet das Programm die Daten an eine API und diese werden dort
weiterverarbeitet. </font>
</p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f"><font size="3" style="font-size: 12pt"><h3>Was
wird dafür benötigt?</h3></font></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f">Grundsätzlich wird zum Installieren von
Paketen in Python </font><font color="#24292f"><b>pip</b></font><font color="#24292f">
verwendet. Falls pip nicht vorhanden ist:</font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#0563c1"><u><a href="https://hellocoding.de/blog/coding-language/python/pip">pip</a></u></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f">Als nächstes wird ein MySQL-Connector
benötigt:</font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#0563c1"><u><a href="https://www.w3schools.com/python/python_mysql_getstarted.asp">MySQL</a></u></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
  
<font color="#24292f">Für den API-Aufruf das Repository downloaden und die .exe ausführen:</font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#0563c1"><u><a href="https://gitlab.com/sh1n1xs/rock-paper-scissors-data-server/-/tree/main">.exe-Datei</a></u></font></p>
  
<font color="#24292f">Für den API-Aufruf in Python:</font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#0563c1"><u><a href="https://www.w3schools.com/python/module_requests.asp">Requests</a></u></font></p>
<p style="line-height: 100%; margin-bottom: 0.17in; background: #ffffff">
<font color="#24292f">Zum Schluss muss noch bei DB.py statt „User“,
der eigene Name bzw. Username eingegeben werden.</font></p>
</body>
</html>
