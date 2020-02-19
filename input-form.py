print("Please enter your name")
name = input()

html = """
<!DOCTYPE html>
<html>
    <head>
      <title>Input Form</title>
      <link href="https://fonts.googleapis.com/css?family=Lacquer&display=swap" rel="stylesheet">
    </head>
    <style>
        body{margin: 0; background: #000; width: 100%; height: 100vh; display: flex; justify-content: center; align-items: center}
        .container{display: flex; flex-direction: column}
        h1{color: #FF0000; margin-bottom: 80px; font-family: Lacquer, sans-serif; text-transform: uppercase; font-size: 80px}
        .form-name{display: flex; justify-content: center}
        #name{width: 500px; padding-bottom: 12px; font-size: 60px; background: #000; border: none; border-bottom: 8px solid #FF0000; color: #FFF; text-align: center; outline: none; font-family: Lacquer, sans-serif; text-transform: uppercase}
    </style>
    <body>
    <div class="container">
      <h1>What's your name?</h1>
      <form action="" method="get" class="form">
        <div class="form-name">
          <input type="text" id="name" required>
        </div>
      </form>
    </div>
    </body> 
  </html>
"""

file = open("index.html", "w")
file.write(html)
file.close()