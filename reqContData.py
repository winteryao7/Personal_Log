from obspy import UTCDateTime
from obspy.clients.fdsn.mass_downloaded import RectangularDomain, Restrictions, MassDownloader

# rectangular region
domain = RectangularDomain(minlatitude=40.8, maxlatitude=42.8,minlongitude=-84.5,maxlongitude=-81.5)

# restriction
restrictions = Restrictions(
    # Get data for target time window
    starttime = obspy.UTCDateTime(2018,10,14),
    endtime = obspy.UTCDateTime(2018,10,20),
    # One file per day
    chunklength_in_sec = 86400,
    # gaps would be dealt with later
    channel="?HZ",
    reject_channels_with_gaps=False,
    # Guard against the same station having different names.
    minimum_interstation_distance_in_m=100.0)

# provider: only IRIS
mdl = MassDownloader(providers=["IRIS"])

# start downloading
mdl.download(domain, restrictions, mseed_storage="waveforms",stationxml_storage="stations")
