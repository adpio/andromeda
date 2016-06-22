# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "crm_brands"
app_title = "BrandsBassadors"
app_publisher = "BrandBassadors"
app_description = "BrandBassadors extensions to the ERPNext platform"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@brandbassadors.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/crm_brands/css/crm_brands.css"
# app_include_js = "/assets/crm_brands/js/crm_brands.js"

# include js, css files in header of web template
# web_include_css = "/assets/crm_brands/css/crm_brands.css"
# web_include_js = "/assets/crm_brands/js/crm_brands.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "crm_brands.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "crm_brands.install.before_install"
# after_install = "crm_brands.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "crm_brands.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"crm_brands.tasks.all"
# 	],
# 	"daily": [
# 		"crm_brands.tasks.daily"
# 	],
# 	"hourly": [
# 		"crm_brands.tasks.hourly"
# 	],
# 	"weekly": [
# 		"crm_brands.tasks.weekly"
# 	]
# 	"monthly": [
# 		"crm_brands.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "crm_brands.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "crm_brands.event.get_events"
# }

