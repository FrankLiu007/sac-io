#!/usr/bin/python3
import struct
import sys
##---------------define a sac_head class-----------------------------------------------
class sac:
	delta=0			# RF time increment, sec    #
	depmin=0.0			#    minimum amplitude      #
	depmax=0.0			#    maximum amplitude      #
	scale=0.0			#    amplitude scale factor #
	odelta=0.0			#    observed time inc      #
	b=0.0			# RD initial time - wrt nz* #
	e=0.0			# RD end time               #
	o=0.0			#    event start            #
	a=0.0			#    1st arrival time       #
	internal1=0.0		#    internal use           #
	t0=0.0			#    user-defined time pick #
	t1=0.0			#    user-defined time pick #
	t2=0.0			#    user-defined time pick #
	t3=0.0			#    user-defined time pick #
	t4=0.0			#    user-defined time pick #
	t5=0.0			#    user-defined time pick #
	t6=0.0			#    user-defined time pick #
	t7=0.0			#    user-defined time pick #
	t8=0.0			#    user-defined time pick #
	t9=0.0			#    user-defined time pick #
	f=0.0			#    event end, sec > 0     #
	resp0=0.0			#    instrument respnse parm#
	resp1=0.0			#    instrument respnse parm#
	resp2=0.0			#    instrument respnse parm#
	resp3=0.0			#    instrument respnse parm#
	resp4=0.0			#    instrument respnse parm#
	resp5=0.0			#    instrument respnse parm#
	resp6=0.0			#    instrument respnse parm#
	resp7=0.0			#    instrument respnse parm#
	resp8=0.0			#    instrument respnse parm#
	resp9=0.0			#    instrument respnse parm#
	stla=0.0			#  T station latititude     #
	stlo=0.0			#  T station longitude      #
	stel=0.0			#  T station elevation, m   #
	stdp=0.0			#  T station depth, m      #
	evla=0.0			#    event latitude         #
	evlo=0.0			#    event longitude        #
	evel=0.0			#    event elevation        #
	evdp=0.0			#    event depth            #
	mag=0.0		#    reserved for future use#
	user0=0.0			#    available to user      #
	user1=0.0			#    available to user      #
	user2=0.0			#    available to user      #
	user3=0.0			#    available to user      #
	user4=0.0			#    available to user      #
	user5=0.0			#    available to user      #
	user6=0.0			#    available to user      #
	user7=0.0			#    available to user      #
	user8=0.0			#    available to user      #
	user9=0.0			#    available to user      #
	dist=0.0			#    stn-event distance, km #
	az=0.0			#    event-stn azimuth      #
	baz=0.0			#    stn-event azimuth      #
	gcarc=0.0			#    stn-event dist, degrees#
	internal2=0.0		#    internal use           #
	internal3=0.0		#    internal use           #
	depmen=0.0			#    mean value, amplitude  #
	cmpaz=0.0			#  T component azimuth     #
	cmpinc=0.0			#  T component inclination #
	xminimum=0.0		#   Minimum value of X (Spectral files only)	#
	xmaximum=0		#    Maximum value of X (Spectral files only)	#
	yminimum=0.0		#    Minimum value of Y (Spectral files only)	#
	ymaximum=0.0		#    Maximum value of Y (Spectral files only)	#
	unused6=0.0		#    reserved for future use#
	unused7=0.0		#    reserved for future use#
	unused8=0.0		#    reserved for future use#
	unused9=0.0		#    reserved for future use#
	unused10=0.0		#    reserved for future use#
	unused11=0.0		#    reserved for future use#
	unused12=0.0		#    reserved for future use#
	nzyear=0			#  F zero time of file, yr  #
	nzjday=0			#  F zero time of file, day #
	nzhour=0			#  F zero time of file, hr  #
	nzmin=0			#  F zero time of file, min #
	nzsec=0			#  F zero time of file, sec #
	nzmsec=0			#  F zero time of file, msec#
	nvhdr=0			#  R header version number  #
	norid=0			#    Origin ID (CSS 3.0)        #
	nevid=0			#    Event ID (CSS 3.0)	         #
	npts=0			# RF number of samples      #
	internal7=0		#    internal use           #
	nwfid=0			#    Waveform ID (CSS 3.0)           #
	nxsize=0		#    Spectral Length (Spectral files only)#
	nysize=0		#    Spectral Width (Spectral files only)#
	unused15=0		#    reserved for future use#
	iftype=0			# RA type of file          #
	idep=0			#    type of amplitude      #
	iztype=0			#    zero time equivalence  #
	unused16=0		#    reserved for future use#
	iinst=0			#    recording instrument   #
	istreg=0			#    stn geographic region  #
	ievreg=0			#    event geographic region#
	ievtyp=0			#    event type             #
	iqual=0			#    quality of data        #
	isynth=0			#    synthetic data flag    	#
	imagtyp=0		#    Magnitude type:			#
	imagsrc=0		#    Source of magnitude information:#
	unused19=0		#    reserved for future use#
	unused20=0		#    reserved for future use#
	unused21=0		#    reserved for future use#
	unused22=0		#    reserved for future use#
	unused23=0		#    reserved for future use#
	unused24=0		#    reserved for future use#
	unused25=0		#    reserved for future use#
	unused26=0		#    reserved for future use#
	leven=0			# RA data-evenly-spaced flag#
	lpspol=0			#    station polarity flag  #
	lovrok=0			#    overwrite permission   #
	lcalda=0			#    calc distance, azimuth #
	unused27=0		#    reserved for future use#
	kstnm=''		#  F station name           #
	kevnm=''		#    event name             #
	kevnm1=''		#    event name             #
	khole=''		#    man-made event name    #
	ko=''			#    event origin time id   #
	ka=''			#    1st arrival time ident #
	kt0=''			#    time pick 0 ident      #
	kt1=''			#    time pick 1 ident      #
	kt2=''			#    time pick 2 ident      #
	kt3=''			#    time pick 3 ident      #
	kt4=''			#    time pick 4 ident      #
	kt5=''			#    time pick 5 ident      #
	kt6=''			#    time pick 6 ident      #
	kt7=''			#    time pick 7 ident      #
	kt8=''			#    time pick 8 ident      #
	kt9=''			#    time pick 9 ident      #
	kf=''			#    end of event ident     #
	kuser0=''		#    available to user      #
	kuser1=''		#    available to user      #
	kuser2=''		#    available to user      #
	kcmpnm=''		#  F component name         #
	knetwk=''		#    network name           #
	kdatrd=''		#    date data read         #
	kinst=''		#    instrument name        #
	data=[]
	def __init__(self):
		pass
	def read(self, fname):
		inf=open(fname,'rb')
		tt=inf.read(4)
		self.delta=struct.unpack('f',tt)
		tt=inf.read(4)
		self.depmim=struct.unpack('f',tt)
		tt=inf.read(4)
		self.depmax=struct.unpack('f',tt)
		tt=inf.read(4)
		self.scale=struct.unpack('f',tt)
		tt=inf.read(4)
		self.odelta=struct.unpack('f',tt)
		tt=inf.read(4)
		self.b=struct.unpack('f',tt)
		tt=inf.read(4)
		self.e=struct.unpack('f',tt)
		tt=inf.read(4)
		self.o=struct.unpack('f',tt)
		tt=inf.read(4)
		self.a=struct.unpack('f',tt)
		tt=inf.read(4)
		self.internal1=struct.unpack('f',tt)
	#-----------------t0-t9----------------------
		tt=inf.read(4)
		self.t0=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t1=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t2=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t3=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t4=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t5=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t6=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t7=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t8=struct.unpack('f',tt)
		tt=inf.read(4)
		self.t9=struct.unpack('f',tt)
	#---------------------------------------
		tt=inf.read(4)
		self.f=struct.unpack('f',tt)
	#---------------resp0-9--------------------------
		tt=inf.read(4)
		self.resp0=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp1=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp2=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp3=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp4=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp5=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp6=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp7=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp8=struct.unpack('f',tt)
		tt=inf.read(4)
		self.resp9=struct.unpack('f',tt)
	#----------------station and event location ---------------------------------
		tt=inf.read(4)
		self.stla=struct.unpack('f',tt)
		tt=inf.read(4)
		self.stlo=struct.unpack('f',tt)
		tt=inf.read(4)
		self.stel=struct.unpack('f',tt)
		tt=inf.read(4)
		self.stdp=struct.unpack('f',tt)
		tt=inf.read(4)
		self.evla=struct.unpack('f',tt)
		tt=inf.read(4)
		self.evlo=struct.unpack('f',tt)
		tt=inf.read(4)
		self.evel=struct.unpack('f',tt)
		tt=inf.read(4)
		self.evdp=struct.unpack('f',tt)
		tt=inf.read(4)
		self.mag=struct.unpack('f',tt)
	#-----------------user0-9---------------------------------
		tt=inf.read(4)
		self.user0=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user1=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user2=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user3=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user4=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user5=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user6=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user7=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user8=struct.unpack('f',tt)
		tt=inf.read(4)
		self.user9=struct.unpack('f',tt)
	#-----------------------------------------
		tt=inf.read(4)
		self.dist=struct.unpack('f',tt)
		tt=inf.read(4)
		self.az=struct.unpack('f',tt)
		tt=inf.read(4)
		self.baz=struct.unpack('f',tt)
		tt=inf.read(4)
		self.gcarc=struct.unpack('f',tt)
		tt=inf.read(4)
		self.internal2=struct.unpack('f',tt)
		tt=inf.read(4)
		self.internal3=struct.unpack('f',tt)
		tt=inf.read(4)
		self.depmen=struct.unpack('f',tt)
		tt=inf.read(4)
		self.cmpaz=struct.unpack('f',tt)
		tt=inf.read(4)
		self.cmpinc=struct.unpack('f',tt)
	#-------------------------------------------
		tt=inf.read(4)
		self.xminimum=struct.unpack('f',tt)
		tt=inf.read(4)
		self.xmaximum=struct.unpack('f',tt)
		tt=inf.read(4)
		self.yminimum=struct.unpack('f',tt)
		tt=inf.read(4)
		self.ymaximum=struct.unpack('f',tt)
	#----------------unuserd6-12-----------------------
		tt=inf.read(4)
		self.unused6=struct.unpack('f',tt)
		tt=inf.read(4)
		self.unused7=struct.unpack('f',tt)
		tt=inf.read(4)
		self.unused8=struct.unpack('f',tt)
		tt=inf.read(4)
		self.unused9=struct.unpack('f',tt)
		tt=inf.read(4)
		self.unused10=struct.unpack('f',tt)
		tt=inf.read(4)
		self.unused11=struct.unpack('f',tt)
		tt=inf.read(4)
		self.unused12=struct.unpack('f',tt)
	#--------------integer number begin-time day -------------------
		tt=inf.read(4)
		self.nzyear=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nzjday=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nzhour=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nzmin=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nzsec=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nzmsec=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nvhdr=struct.unpack('i',tt)
		tt=inf.read(4)
		self.norid=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nevid=struct.unpack('i',tt)
	#------------------------------------------
		tt=inf.read(4)
		self.npts=struct.unpack('i',tt)
		tt=inf.read(4)
		self.internal7=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nwfid=struct.unpack('i',tt)
		tt=inf.read(4)
		self.nxsize=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused15=struct.unpack('i',tt)
		tt=inf.read(4)
		self.iftype=struct.unpack('i',tt)
		tt=inf.read(4)
		self.idep=struct.unpack('i',tt)
		tt=inf.read(4)
		self.iztype=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused16=struct.unpack('i',tt)
	#------------------------------------------------------
		tt=inf.read(4)
		self.iinst=struct.unpack('i',tt)
		tt=inf.read(4)
		self.istreg=struct.unpack('i',tt)
		tt=inf.read(4)
		self.ievreg=struct.unpack('i',tt)
		tt=inf.read(4)
		self.ievtyp=struct.unpack('i',tt)
		tt=inf.read(4)
		self.iqual=struct.unpack('i',tt)
		tt=inf.read(4)
		self.isynth=struct.unpack('i',tt)
		tt=inf.read(4)
		self.imagtyp=struct.unpack('i',tt)
		tt=inf.read(4)
		self.imagsrc=struct.unpack('i',tt)
	#------------------unused19-26-------------------------------------
		tt=inf.read(4)
		self.unused19=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused20=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused21=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused22=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused23=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused24=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused25=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused26=struct.unpack('i',tt)
	#-------------------------------------------------------
		tt=inf.read(4)
		self.leven=struct.unpack('i',tt)
		tt=inf.read(4)
		self.lpspol=struct.unpack('i',tt)
		tt=inf.read(4)
		self.lovrok=struct.unpack('i',tt)
		tt=inf.read(4)
		self.lcalda=struct.unpack('i',tt)
		tt=inf.read(4)
		self.unused27=struct.unpack('i',tt)
	#-----------integer number end and string begin--------------------------
		tt=inf.read(8)
		self.kstnm=struct.unpack('8c',tt)
		tt=inf.read(16)
		self.kevnm=struct.unpack('16c',tt)
		tt=inf.read(8)
		self.khole=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.ko=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.ka=struct.unpack('8c',tt)
	#------------------kt0-9--------------------------------
		tt=inf.read(8)
		self.kt0=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt1=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt2=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt3=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt4=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt5=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt6=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt7=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt8=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kt9=struct.unpack('8c',tt)
	#------------------------------------------------
		tt=inf.read(8)
		self.kf=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kuser0=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kuser1=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kuser2=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kcmpnm=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.knetwk=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kdatrd=struct.unpack('8c',tt)
		tt=inf.read(8)
		self.kinst=struct.unpack('8c',tt)
	#--------------------read data------------------------------------
		data=[]
		for i in range(0,self.npts):
			tt=inf.read(4)
			tt=struct.unpack('f',tt)
			data.append(tt)
		inf.close()
		print(sach)



###------------this line below not used----------------

