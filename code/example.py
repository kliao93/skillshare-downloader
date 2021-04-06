from downloader import Downloader

cookie = """
muted=false; muted=false; device_session_id=e045e92c-efe6-4d89-b7ed-ef709643a822; show-like-copy=1; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; _gcl_au=1.1.224059419.1616378861; __pdst=d921b2a352564c2eac526764618a00e3; _ga=GA1.2.1722488104.1616378862; sm_uuid=1616379192585; _scid=bb6f4b3e-48b5-419a-8cde-5975a04f7d7c; _pin_unauth=dWlkPU56STJNRGsyTUdZdE1qSTJNQzAwWVRkbUxUaGpaakV0WlRnNE9UQmtZV001TldFNQ; __qca=P0-718291786-1616378864309; __stripe_mid=7fe38618-8998-4ef4-9b23-640bb90b889cd4d8ad; __ssid=7a45b9808208ee32036b2fbb6efd184; G_ENABLED_IDPS=google; _gid=GA1.2.2115502493.1617590784; _sctr=1|1617508800000; dismiss_transcripts_tooltip=1; _uetsid=1b8ed44095b911ebbc2b6d8724f9673a; _uetvid=627c95e08ab311ebbaad5366ec8a867d; IR_PI=e57b8abd-8ab3-11eb-8951-02caec40f184%7C1617694831959; _derived_epik=dj0yJnU9bkpRNkZHTmJlcFB5WGpRNmNybnVNWmNFcGFYR3VCSFEmbj13UFVvRkNzX25YbDNMMTlLUl9MZk5RJm09MSZ0PUFBQUFBR0JxdnZBJnJtPTEmcnQ9QUFBQUFHQnF2dkE; YII_CSRF_TOKEN=OTRCMVdpMWxKWnQ2bFA2RVBEelhmeWNuTXFsUHN3d1bKhYvrrxEdXqStLfSA-x-kPAxXp3zM9p_57qwEg6w-eg%3D%3D; PHPSESSID=c57945201c8c3d70b015c6c8a761e0bc
"""

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Productivity-Masterclass-Create-a-Custom-System-that-Works/442860604')

# or by class ID:
# dl.download_course_by_class_id(442860604)
