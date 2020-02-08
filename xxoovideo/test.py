from scrapy.utils.project import get_project_settings
setting = get_project_settings()
print(setting.get("BOT_NAME"))
