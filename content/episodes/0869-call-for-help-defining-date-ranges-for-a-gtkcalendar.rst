Call for help: defining date ranges for a gtk.Calendar
######################################################
:slug: call-for-help-defining-date-ranges-for-a-gtkcalendar
:date: 2008-12-08 19:17
:category:
:tags: english

I’ve re-designed the dialog for adding or editing a bill for my pet
project BillReminder and am now in need of help to improve the user
interface a bit more before releasing another version. I figured someone
out there may either have the answer or have more free time at their
disposal than me. :)

Here’s what the dialog looks like right now:

|BillReminder new dialog for recurring bills|

The issue is related to the option of adding recurring bills, which a
user can do by changing the **Repeat** field to something other than
**Once** (i.e. **Monthly**, **Weekly**). This will enable the **End
Date** field, a customized widget that uses a gtk.Calendar to allow the
user to define how far into the future to automatically create instances
of the bill being entered. I want to be able to define a start and end
date for the catalog, so that the user doesn’t pick a date which is
prior to the **Due Date**. In other words, if the due date is tomorrow,
don’t allow the user to set the end date to yesterday. A couple of use
cases that have to be taken into consideration are:

-  When adding a new bill, the end date can not be earlier/less than the
   due date; therefore, every time the user changes the due date, the
   end date should be automatically updated to be at least equals to the
   due date;
-  If the end date and due date are equal and the user chose **Monthly**
   or Weekly for the **Repeat** field, a dialog should pop up alerting
   that only one instance will be created;
-  If editing an existing bill, the **Repeat** and **End Date** are
   disabled; however, changing the **Due Date** should still update the
   value for **End Date** (for cosmetic reasons);

So, is there anyone out there with time in their hands who would like to
take a crack at it? If so, please add your comments and (preferably)
patches to `this <http://bugzilla.gnome.org/show_bug.cgi?id=563736>`__
bug report.

.. |BillReminder new dialog for recurring bills| image:: http://farm4.static.flickr.com/3139/3093367080_59f76bd9c0_o.png
   :target: http://www.flickr.com/photos/ogmaciel/3093367080/
