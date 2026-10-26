[app]
title = Amar AI
package.name = amarai
package.domain = com.skmastafa.amarai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

# --- Android fix ---
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
