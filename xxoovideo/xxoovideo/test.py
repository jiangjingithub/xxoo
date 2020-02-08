from scrapy.utils.project import get_project_settings
setting = get_project_settings()
s = setting.get("FILES_STORE")
print(s)