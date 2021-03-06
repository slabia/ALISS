from django.test import TestCase
from django.test import Client
from django.urls import reverse
from aliss.tests.fixtures import Fixtures
from aliss.models import *

class v4ServiceAreaSpatialDataViewTestCase(TestCase):

    def setUp(self):
      self.service = Fixtures.create()
      self.client = Client()
      self.service_area = ServiceArea.objects.create(name="Glasgow City", code="S12000046", type=2)
      self.service.service_areas.add(self.service_area)
      self.json = [
        {
            "type": "Feature",
            "properties": {
                "objectid": 367,
                "lad18cd": "S12000046",
                "lad18nm": "Glasgow City",
                "lad18nmw": " ",
                "bng_e": 261534,
                "bng_n": 667033,
                "long": -4.21478987,
                "lat": 55.87649918,
                "st_lengthshape": 87924.48121595873,
                "st_areashape": 178587434.4940189
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            -4.22757646963653,
                            55.84081553872844
                        ],
                        [
                            -4.220433264726125,
                            55.83310425737028
                        ],
                        [
                            -4.203007300727329,
                            55.844130518897764
                        ],
                        [
                            -4.198829334532107,
                            55.83364798685698
                        ],
                        [
                            -4.1804898990481405,
                            55.83560899707189
                        ],
                        [
                            -4.172507226824287,
                            55.82296684476971
                        ],
                        [
                            -4.130597432692027,
                            55.833279606480424
                        ],
                        [
                            -4.11115145611575,
                            55.82586813565916
                        ],
                        [
                            -4.107031799473984,
                            55.83465258585653
                        ],
                        [
                            -4.102168742410194,
                            55.84250963744821
                        ],
                        [
                            -4.074704107764738,
                            55.84411998674332
                        ],
                        [
                            -4.088392245481783,
                            55.85384163365652
                        ],
                        [
                            -4.07170515706163,
                            55.861265911112824
                        ],
                        [
                            -4.0788068400535575,
                            55.88159950475184
                        ],
                        [
                            -4.125307155035274,
                            55.88806399060322
                        ],
                        [
                            -4.164381219874791,
                            55.883579446485044
                        ],
                        [
                            -4.161513411101066,
                            55.89796798928821
                        ],
                        [
                            -4.180416081418078,
                            55.90490867347386
                        ],
                        [
                            -4.23635858978936,
                            55.896837124435116
                        ],
                        [
                            -4.268383291163433,
                            55.9284934924348
                        ],
                        [
                            -4.29804968016659,
                            55.92916718621031
                        ],
                        [
                            -4.301264046518112,
                            55.91636316093881
                        ],
                        [
                            -4.290421039505743,
                            55.91179233824439
                        ],
                        [
                            -4.327840412927068,
                            55.899689581141544
                        ],
                        [
                            -4.348485417356666,
                            55.90523469625339
                        ],
                        [
                            -4.346215139629732,
                            55.916491741547055
                        ],
                        [
                            -4.379617070281586,
                            55.92098003574179
                        ],
                        [
                            -4.38995268453848,
                            55.91051121707005
                        ],
                        [
                            -4.375474565129326,
                            55.900024310313725
                        ],
                        [
                            -4.393185434590535,
                            55.889146094405824
                        ],
                        [
                            -4.353433592083708,
                            55.87373892258495
                        ],
                        [
                            -4.364671452280923,
                            55.855324020386945
                        ],
                        [
                            -4.3808725531791355,
                            55.856341638812914
                        ],
                        [
                            -4.368029290969201,
                            55.84543955689139
                        ],
                        [
                            -4.381413610864957,
                            55.82314784365725
                        ],
                        [
                            -4.367452746966189,
                            55.81770031827132
                        ],
                        [
                            -4.372059266506329,
                            55.79476489137978
                        ],
                        [
                            -4.333448420839391,
                            55.79287413281156
                        ],
                        [
                            -4.3262378658889675,
                            55.80844527340661
                        ],
                        [
                            -4.29262476699183,
                            55.813935584676024
                        ],
                        [
                            -4.260682240293996,
                            55.811014284814924
                        ],
                        [
                            -4.268245839347655,
                            55.791639837344164
                        ],
                        [
                            -4.25074091092872,
                            55.784885787523535
                        ],
                        [
                            -4.226698115233537,
                            55.781274889272446
                        ],
                        [
                            -4.2239299554509,
                            55.79194394392795
                        ],
                        [
                            -4.204285017833057,
                            55.800446051142366
                        ],
                        [
                            -4.214529591879311,
                            55.8150721321777
                        ],
                        [
                            -4.22548763203423,
                            55.81217257653224
                        ],
                        [
                            -4.233751583019541,
                            55.81865629355188
                        ],
                        [
                            -4.22757646963653,
                            55.84081553872844
                        ]
                    ]
                ]
            }
        }
    ]

    def test_get_feature(self):
        path = '/api/v4/service-area-spatial/?service_id=' + str(self.service.pk)
        response = self.client.get(path, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.data, self.json)

    def test_get_full_dataset(self):
        path = '/api/v4/service-area-spatial/full-set/?type=2'
        response =  self.client.get(path, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_dataset_name_key(self):
        path = '/api/v4/service-area-spatial/full-set/?type=0'
        response =  self.client.get(path, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name_key'], 'ctry17nm')

    def tearDown(self):
        self.service.delete()
        self.service_area.delete()
        for organisation in Organisation.objects.filter(name="TestOrg"):
            organisation.delete()
