import constants
import os
import pandas as pd
import json


def pid_to_pt(pid):
    return f'p{pid:02d}'


def get_pt_path(pid):
    return os.path.join(constants.base_dir, pid_to_pt(pid))


def get_fitbit_path(pid):
    return os.path.join(get_pt_path(pid), constants.fitbit_dir)


def get_docs_path(pid):
    return os.path.join(get_pt_path(pid), constants.docs_dir)


def get_pmsys_path(pid):
    return os.path.join(get_pt_path(pid), constants.pmsys_dir)

# get_calories(1)
# OK
def get_calories(pid):
    filename = 'calories.json'
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename)).rename(columns={"value":"calories"})

# OK
def get_distance(pid):
    filename = 'distance.json'
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename)).rename(columns={"value":"distance"})


# TODO: Nested JSON's?
def get_exercise(pid):
    filename = 'exercise.json'
    kept_columns = [
        'logId',
        'activityName',
        'activityTypeId',
        'activityLevel',
        'averageHeartRate',
        'calories',
        'activeDuration',
        'steps',
        'startTime',
        'elevationGain'
    ]
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename))[kept_columns]

# OK
def get_hr(pid):
    filename = 'heart_rate.json'
    df = pd.read_json(os.path.join(get_fitbit_path(pid), filename))
    df['bpm'] = df['value'].apply(lambda x:x['bpm'])
    kept_columns = [
        'dateTime',
        'bpm'
    ]
    return df[kept_columns]


# OK
def get_laminutes(pid):
    filename = 'lightly_active_minutes.json'
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename)).rename(columns={'value':'laminutes'})


# OK
def get_maminutes(pid):
    filename = 'moderately_active_minutes.json'
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename)).rename(columns={'value':'maminutes'})


# OK
def get_resthr(pid):
    filename = 'resting_heart_rate.json'
    df = pd.read_json(os.path.join(get_fitbit_path(pid), filename))
    df['resthr'] = df['value'].apply(lambda x:x['value'])
    kept_columns = [
        'dateTime',
        'resthr'
    ]
    return df[kept_columns]


# OK
def get_sedminutes(pid):
    filename = 'sedentary_minutes.json'
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename)).rename(columns={'value':'sedminutes'})


# OK
def get_sleep(pid):
    filename = 'sleep.json'
    df = pd.read_json(os.path.join(get_fitbit_path(pid), filename))
    #df['deepCount'] = df['levels'].apply(lambda x:x['summary']['deep']['count'])
    #df['deepMinutes'] = df['levels'].apply(lambda x:x['summary']['deep']['minutes'])
    # df['lightCount'] = df['levels'].apply(lambda x: x['summary']['light']['count'])
    # df['lightMinutes'] = df['levels'].apply(lambda x: x['summary']['light']['minutes'])
    # df['remCount'] = df['levels'].apply(lambda x: x['summary']['rem']['count'])
    # df['remMinutes'] = df['levels'].apply(lambda x: x['summary']['rem']['minutes'])
    # df['wakeCount'] = df['levels'].apply(lambda x: x['summary']['wake']['count'])
    kept_columns = [
        'logId',
        'dateOfSleep',
        'startTime',
        'endTime',
        'duration',
        'minutesToFallAsleep',
        'minutesAsleep',
        'minutesAwake',
        'minutesAfterWakeup',
        'timeInBed',

    ]
    """
    'deepCount',
        'deepMinutes',
        'lightCount',
        'lightMinutes',
        'remCount',
        'remMinutes',
        'wakeCount'
    """
    return df[kept_columns]


# OK
def get_sleepscore(pid):
    filename = 'sleep_score.csv'
    return pd.read_csv(os.path.join(get_fitbit_path(pid), filename))


# OK
def get_steps(pid):
    filename = 'steps.json'
    df = pd.read_json(os.path.join(get_fitbit_path(pid), filename))
    df = df.rename(columns={"value":"steps"})
    return df


# OK
def get_vaminutes(pid):
    filename = 'very_active_minutes.json'
    return pd.read_json(os.path.join(get_fitbit_path(pid), filename)).rename(columns={'value':'vaminutes'})
