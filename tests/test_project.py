import pytest
from project0 import project0
incident_url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-01_daily_incident_summary.pdf"
db = 'normanpd.db'
def test_fetchincidents():
    result = project0.fetchincidents(incident_url)
    assert result is not None
def test_extractincident():
    incident_data = project0.fetchincidents(incident_url)
    incidents = project0.extractincidents(incident_data)
    for items in incidents:
        assert len(items) == 5
def test_populatedb():
    incident_data = project0.fetchincidents(incident_url)
    incidents = project0.extractincidents(incident_data)
    dbresult = project0.populatedb(db,incidents)
    assert dbresult is None


def test_createdbtest():
    testresult = project0.createdb()
    assert db == testresult
def test_status():
    result = project0.status()
    assert result is None
