from bug.models import *
from report.models import *

def execute():
    bug_effor_obj = BugEffort.objects.all()

    for beo in bug_effor_obj:
        # create new record us_bug and effort date match doesn't exit
        wsr_obj = WeeklyStatusReport(us_bug_id=beo.bug_obj.board_id,
                                     us_bug_details=beo.bug_obj.bug_title,
                                     assgined_to=beo.assgined_to,
                                     efforts=beo.spend_hr,
                                     effort_date=beo.effort_date)

        wsr_obj.save()
        print ("record created")

if __name__ == "__main__":
    execute()
