# Create Timesheets upon Time Off Validation

Odoo automatically timesheets on project/tasks upon time off requests. This
allows for better overall control over the validation of timesheets, as it
does not leave place for forgetfulness and questions after hours that have not
been timesheeted by the employee.

Activate the [developer mode](../../../general/developer_mode.html#developer-
mode), go to _Timesheets_ , and change the _Project_ and _Task_ set by
default, if you like.

![View of Timesheets setting enabling the feature record time off in Odoo
Timesheets](../../../../_images/record_time_off.png)

Go to Time Off ‣ Configuration ‣ Time Off Types. Select or create the needed
type, and decide if you would like the requests to be validated or not.

![View of a time off types form emphasizing the time off requests and
timesheets section in Odoo Time Off](../../../../_images/time_off_types.png)

Now, once the employee has requested his time off and the request has been
validated (or not, depending on the setting chosen), the time is automatically
allocated on _Timesheets_ , under the respective project and task.

On the example below, the user requested _Paid Time off_ from July 13th to
15th.

![View of the time off request form in Odoo Time
Off](../../../../_images/time_off_request.png)

Considering that validation is not required, the requested time off is
automatically displayed in _Timesheets_. If validation is necessary, the time
is automatically allocated after the responsible person for validating does it
so.

![Video of timesheets emphasizing the requested time off from the employee in
Odoo Timesheets](../../../../_images/timesheets.png)

Click on the magnifying glass, hovering over the concerned cell, to access all
the aggregated data on that cell (day), and see details regarding the
project/task.

![View of the details of a project/task in Odoo
Timeheets](../../../../_images/timesheet_description.png)

