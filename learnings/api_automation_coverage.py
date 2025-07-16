from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

# Create a new Workbook
wb = Workbook()

# Select the active worksheet
ws = wb.active

# Data
total_apis = 28
automated_apis = 23
out_of_scope_apis = 5
automation_coverage = (automated_apis / total_apis) * 100
not_automated_percentage = (out_of_scope_apis / total_apis) * 100

# Write data to worksheet
ws.append(["Total APIs", total_apis])
ws.append(["APIs (Automated)", automated_apis])
ws.append(["Out of Scope APIs", out_of_scope_apis])
ws.append(["Automation Coverage (%)", automation_coverage])
ws.append(["APIs Not Automated (%)", not_automated_percentage])

# Add pie chart for automation coverage
chart_automation = PieChart()
labels_automation = Reference(ws, min_col=1, min_row=2, max_row=4)
data_automation = Reference(ws, min_col=2, min_row=2, max_row=4)
chart_automation.add_data(data_automation, titles_from_data=True)
chart_automation.set_categories(labels_automation)
chart_automation.title = "API Automation Coverage"

# Add data labels with percentages
data_points = chart_automation.series[0]
data_points.data_labels = Reference(ws, min_col=3, min_row=2, max_row=4)

# Add pie chart for APIs not automated
chart_not_automated = PieChart()
labels_not_automated = Reference(ws, min_col=1, min_row=5, max_row=5)
data_not_automated = Reference(ws, min_col=2, min_row=5, max_row=5)
chart_not_automated.add_data(data_not_automated, titles_from_data=True)
chart_not_automated.set_categories(labels_not_automated)
chart_not_automated.title = "APIs Not Automated"

# Add data labels with percentages
data_points = chart_not_automated.series[0]
data_points.data_labels = Reference(ws, min_col=3, min_row=5, max_row=5)

# Add charts to worksheet
ws.add_chart(chart_automation, "D2")
ws.add_chart(chart_not_automated, "D18")

# Save the workbook
wb.save("API_Automation_Statistics.xlsx")
