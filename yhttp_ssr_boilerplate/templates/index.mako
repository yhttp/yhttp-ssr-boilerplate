<%inherit file="master.mako" />

<%block name="head">
  <meta property="og:title" content="YHTTP SSR Boilerplate">
  <meta property="og:type" content="website">
  <meta property="og:url" content="${settings.publicurl.rstrip('/')}/">
</%block>

<section class="home" aria-labelledby="home-title">
  <h1 id="home-title">Your server-rendered app starts here</h1>
  <p>Rendered on the server with YHTTP and Mako.</p>
</section>
