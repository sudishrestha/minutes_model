#-*- coding: utf-8 -*-
from openerp import models, fields, api, tools

class meeting_minutes(models.Model):
	_name = 'meeting.information'
	_description = 'Information'
	state = fields.Selection([('create', 'Create'),('meeting', 'Meeting'),('minutes', 'Minutes'),],default='create')

	#_inherits = {'meeting.venue': 'mod_id'}
	
	#_inherits = {'meeting.participant': 'part_id' ,'meeting.agenda': 'agenda_id'}

        meet_type= fields.Char('Meeting Type', size=64)
        meeting_date= fields.Date('Meeting Date')
        #meeting_time=fields.Time('Meeting Time', required=True)
        meeting_purpose= fields.Char('Meeting Purpose', size=64)
	meeting_moderator = fields.Char('Meeting Moderator', size=64)

        participant_ids=fields.One2many('meeting.participant','participant_id2',string = 'participant')
	agenda_ids = fields.One2many('meeting.agenda', 'agenda_no', string= "Agenda")
	venue_fk = fields.Many2one('meeting.venue',string = "Select Venue")	

	discussion_id1 = fields.One2many('meeting.discussion', 'meeting_no', string= "Discussion")	
        attendance_id= fields.One2many('meeting.attendance', 'attendance_id1', string= "Attendance")
	decision_id = fields.One2many('meeting.decision', 'meeting_id', string= "Decision")
	@api.multi
	def concept_progressbar(self):
		self.ensure_one()
		self.write({'state': 'create',})

    
    #This function is triggered when the user clicks on the button 'In progress'
	@api.multi
	def progress_progressbar(self):
		self.ensure_one()
		self.write({'state': 'meeting'})

    #This function is triggered when the user clicks on the button 'Done'
	@api.multi
	def done_progressbar(self):
		self.ensure_one()
		self.write({'state': 'minutes',})
class meeting_venue(models.Model):
	_name = 'meeting.venue'
	_description = 'Meeting Venue'
	venue_fks = fields.One2many('meeting.information','venue_fk',string = "Venue ids")
	venue_id=fields.Integer('Venue ID')
        venue_name= fields.Char('Venue', size=64)
        venue_address= fields.Char('Venue Address',size=64)

class Participant(models.Model):
	_name = 'meeting.participant'
        participant_id2= fields.Many2one('meeting.information','Meeting')
	attendance_id = fields.One2many('meeting.attendance', 'attendance_id', string= "Attendance")
        participant_name= fields.Char('Participant Name', size=64)
        email_id=fields.Char('Email Address')
        department= fields.Char('Department Name')
        phone_number= fields.Char('Phone Number')
class Agenda(models.Model):
	_name = 'meeting.agenda'
	agenda_no = fields.Many2one('meeting.information','Meeting')
        agenda_name= fields.Char('Agenda Name', size=64)
        remarks= fields.Char('Agenda Remarks')
        agenda_owner= fields.Char('Agenda Owner', size=64)
	discussion_id3 = fields.One2many('meeting.discussion', 'discussion_id1', string= "Discussion")
	decision_id = fields.One2many('meeting.decision', 'agenda_id', string= "Decision")

class Discussion(models.Model):
	_name = 'meeting.discussion'
	discussion_id1 = fields.Many2one('meeting.agenda','Agenda')
	meeting_no = fields.Many2one('meeting.information','Meeting')
        discussion_content= fields.Char('Discussion')
        participant_id= fields.Char("Partcipant")
class attendance(models.Model):
	_name ='meeting.attendance'
        attendance_id= fields.Many2one('meeting.participant','Participant')
        attendance_id1= fields.Many2one('meeting.information','Meeting')
        attendance=fields.Boolean('Present/Absent',default = "True")
class Decision(models.Model):
	_name='meeting.decision'
	meeting_id = fields.Many2one('meeting.information','Meeting')
	agenda_id = fields.Many2one('meeting.agenda','Agenda')
	decision_name= fields.Char('Decision')
	decision_remarks=fields.Char('Remarks')
	


