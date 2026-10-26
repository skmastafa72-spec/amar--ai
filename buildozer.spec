[app]
title = Amar AI
package.name = amarai
package.domain = org.amar.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.fork = kivy
p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
