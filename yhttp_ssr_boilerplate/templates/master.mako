<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="A clean foundation for server-rendered YHTTP applications.">
    <title>YHTTP SSR Boilerplate</title>
    % if settings.env == 'development':
      <script type="module" src="${asseturl('@vite/client')}"></script>
    % endif
    <link rel="stylesheet" href="${asseturl('www/master.css')}">
    % if hasattr(next, 'head'):
      ${next.head()}
    % endif
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="/">YHTTP SSR Boilerplate</a>
    </header>
    <main>
      ${self.body()}
    </main>
    <script type="module" src="${asseturl('www/master.js')}"></script>
  </body>
</html>
