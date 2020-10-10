<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Pashmak programming language online interpreter</title>
    <link rel="stylesheet" href="static/css/bootstrap.min.css" />
    <style>
    body{
        background-color: #222;
        color: #eee;
    }
    .code-font{
        
    }
    </style>
</head>
<body>
    <div class="container">
        <h1>Pashmak programming language online interpreter</h1>
        <form method="POST" class="form-group">
            <textarea style="background-color: #555; color: #eee; min-height: 300px;" class="form-control" placeholder="write your code..." name="code"><?= htmlspecialchars($code) ?></textarea>
            <textarea style="background-color: #555; color: #eee; min-height: 100px;" class="form-control" placeholder="program stdin inputs" name="stdin"><?= htmlspecialchars($stdin) ?></textarea>
            <input class="btn btn-dark" style="width: 100%; margin-top: 10px;" type="submit" value="run" />
        </form>
        <?php if($output !== null): ?>
        <pre style="background-color: #000; color: #fff;" class="code-font"><?= htmlspecialchars($output); ?></pre>
        <?php endif; ?>
        <hr />
        <a href="https://github.com/parsampsh/pashmak" target="_blank">Github</a>
        &nbsp;&nbsp;&nbsp;
        <a href="https://github.com/parsampsh/pashmak/blob/master/README.md#documentation" target="_blank">Pashmak Documentation</a>
        <br />
        <span style="color: gray;">sorry for website bullshit design, i'm not designer</span>
        <br />
    </div>
</body>
</html>
