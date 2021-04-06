from downloader import Downloader

cookie = """
"muted=false; muted=false; device_session_id=e045e92c-efe6-4d89-b7ed-ef709643a822; show-like-copy=1; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; _gcl_au=1.1.224059419.…"
"""

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Productivity-Masterclass-Create-a-Custom-System-that-Works/442860604')

# or by class ID:
# dl.download_course_by_class_id(442860604)
