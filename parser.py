from asyncio.windows_events import NULL
import json

from patient import *

patients = []
    
def parse(fn):
    with open(fn) as fn:
        d = json.load(fn)

    for i in d:
        if i == 'PatientInformation':
            # from PatientInformation: name/surname, gender, diagnosis, implant_date
            # from LeadConfiguration: hemisphere, lead_location
            v = d[i]['Initial']
            patient = Patient(v['PatientFirstName'], v['PatientLastName'], v['PatientGender'], v['Diagnosis'], NULL)
        elif i == 'DeviceInformation':   
            v = d[i]['Initial']
            patient.implant_date = v['ImplantDate']
        elif i == 'IndefiniteStreaming':
            v = d[i]
            for v1 in v:
                times = list(map(int, (filter(None, v1['TicksInMses'].split(',')))))
                channel = v1['Channel']
                global_packet_sizes= list(map(int, (filter(None, v1['GlobalPacketSizes'].split(',')))))
                sample_rate_hz = v1['SampleRateInHz']
                time_domain_data = v1['TimeDomainData']

                patient.channel_coordinates.append([channel, times, sample_rate_hz, global_packet_sizes, time_domain_data])
            patients.append(patient)
        elif i == 'BrainSenseTimeDomain':
            v = d[i]
            for v1 in v:
                times = list(map(int, (filter(None, v1['TicksInMses'].split(',')))))
                channel = v1['Channel']
                global_packet_sizes= list(map(int, (filter(None, v1['GlobalPacketSizes'].split(',')))))
                sample_rate_hz = v1['SampleRateInHz']
                time_domain_data = v1['TimeDomainData']

                patient.channel_coordinates.append([channel, times, sample_rate_hz, global_packet_sizes, time_domain_data])
            patients.append(patient)
        # elif i == 'BrainSenseLfp':
        #     # from BrainSenseLfp: [{ LfpData: [{ TicksInMs: int, Right: { LFP: int } Left: { LFP: int }}]}]
        #     v = d[i][0]['LfpData'] # this needs to go one level deeper and iterate
        #     for v1 in v:
        #         time = v1['TicksInMs']
        #         right_lfp = v1['Right']['LFP']
        #         left_lfp = v1['Left']['LFP']

        #         patient.coordinates.append([time, right_lfp, left_lfp])
        #     patients.append(patient)
