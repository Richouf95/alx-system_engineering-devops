# 0x19. Postmortem

![alt postmortem](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif)

## Issue Summary
For a period of 2 hours, from 2:00 pm to 4:00 pm (local time), our Apache service encountered a 500 error, resulting in a partial interruption of our website. This affected around 30% of our users, who experienced difficulties accessing and browsing the site.

## Timeline
- 2:00 pm - 4:00 pm: Detection of error 500 on the website through automatic performance monitoring.
- 2:15pm: An alert is sent to the IT operations team, signalling a drop in site availability.
- 2:20pm: Engineers begin examining Apache's access and error logs to identify the cause of the error.
- 2:30 pm: A possible configuration problem in the PHP parameter file is hypothesized.
- 14:45: Attempts to restart the Apache server and reload the PHP configuration are made without success.
- 15:00: The incident is escalated to the web development team for further investigation.
- 15:30: Further analysis reveals a configuration error in the wp-settings.php file, causing error 500.
- 15h45: A temporary correction is applied by manually modifying the wp-settings.php file on the server to correct the erroneous configuration.
- 4:00 pm: The website is back online after the correction has been applied.


## Root cause and resolution
The root cause of error 500 was a configuration error in the wp-settings.php file, where an incorrect reference to a PHP module was introduced. This was corrected by manually editing the wp-settings.php file on the server to correct the incorrect reference.


## Corrective and preventive measures
- Correct the wp-settings.php file to remove the incorrect reference to the PHP module.
- Set up automated tests to verify the configuration of the wp-settings.php file for future deployments.
- Reinforce procedures for validating configuration changes to avoid similar errors in the future.
- Update system documentation to include clear instructions on the correct configuration of wp-settings.php.

By taking these corrective and preventive measures, we aim to minimize similar service interruptions in the future and enhance the stability and reliability of our web system.

