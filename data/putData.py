# -*- coding: utf-8 -*-
import boto3
import hashlib
import sys

if len(sys.argv) > 1:
	tableName = sys.argv[1]

	print "Putting data in DyanmoDB table: " + tableName

	session = boto3.Session(profile_name='kayaklaunch')

	ddb = session.client('dynamodb')

	routeName = 'Bönigen to Iseltwlad'
	ddb.put_item(
		TableName = tableName,
		Item={
			'latlon': {
				'M': {
					'start': {
						'S': '7.898166859522462,46.68859340250492'
					},
					'end': {
						'S': '7.965998835861683,46.711253290995955'
					}
				}
			},
			'distance': {
				'N': '14'
			},
			'paddlingTimes': {
				'M': {
					'kayak': {
						'S': '2.5 - 3 hours'
					},
					'canoe': {
						'S': '3.5 - 4 hours'
					},
					'sup': {
						'S': '3.5 - 4 hours'
					}
				}
			},
			'name': {
				'S': routeName
			},
			'urlWeather': {
				'S': 'https://www.meteoblue.com/en/weather/widget/daily/iseltwald_switzerland_2660246?geoloc=fixed&days=7&tempunit=CELSIUS&windunit=KILOMETER_PER_HOUR&precipunit=MILLIMETER&coloured=coloured&pictoicon=0&pictoicon=1&maxtemperature=0&maxtemperature=1&mintemperature=0&mintemperature=1&windspeed=0&windspeed=1&windgust=0&windgust=1&winddirection=0&winddirection=1&uv=0&uv=1&humidity=0&precipitation=0&precipitation=1&precipitationprobability=0&precipitationprobability=1&spot=0&pressure=0&layout=light'
			},
			'hazards': {
				'M': {
					'environment': {
						'SS': ['Cliffs make short portions of the route \u201ccommitted\u201d, meaning there\u2019s no quick exit from the water', 'Submerged rocks are present in the shallow waters, where the cliffs give way to rocky shores']
					},
					'wildlife': {
						'SS': ['No wildlife hazards known']
					},
					'weather': {
						'SS': ['Significant changes in weather can occur during the day, due to the mountainous terrain', 'Small waves can form in stronger winds']
					},
					'traffic': {
						'SS': ['Ferries dock at the piers in both Bönigen and Iseltwlad regularly. Local laws require paddle craft stay 50m away from them at all time', 'Private boats and white-water rafts often use the boat ramps in Bönigen during the summer months', 'Private boats enter and exit the harbour in Bönigen regularly']
					}
				}
			},
			'routeID': {
				'S': hashlib.sha1(routeName).hexdigest()[-8:]
			},
			'location': {
				'S': 'Brienzersee'
			},
			'urlMap': {
				'S': 'https://raw.githubusercontent.com/binghamchris/kayaklaun.ch/gh-pages/map/iseltwald.kml'
			},
			'descriptionShort': {
				'S': "A relaxed paddle along Lake Brienz's southern shore to the lake side village of Iseltwald. Ideal as a day trip with a stop for a leisurely lunch."
			},
			'urlHeadlineImg': {
				'S': 'https://raw.githubusercontent.com/binghamchris/kayaklaun.ch/gh-pages/img/iseltwald-background.jpg'
			},
			'type': {
				'S': 'A-B'
			}
		}
	)

	routeName = 'Lachen Round Trip'
	ddb.put_item(
		TableName = tableName,
		Item={
			'latlon': {
				'M': {
					'start': {
						'S': '8.863591784611344,47.2034752741456'
					},
					'end': {
						'S': '8.864019177854061,47.20354853197932'
					}
				}
			},
			'distance': {
				'N': '16'
			},
			'paddlingTimes': {
				'M': {
					'kayak': {
						'S': '3 - 3.5 hours'
					},
					'canoe': {
						'S': '4 - 4.5 hours'
					},
					'sup': {
						'S': '4 - 4.5 hours'
					}
				}
			},
			'name': {
				'S': routeName
			},
			'urlWeather': {
				'S': 'https://www.meteoblue.com/en/weather/widget/daily/lachen_switzerland_2660075?geoloc=fixed&amp;days=7&amp;tempunit=CELSIUS&amp;windunit=KILOMETER_PER_HOUR&amp;precipunit=MILLIMETER&amp;coloured=coloured&amp;pictoicon=0&amp;pictoicon=1&amp;maxtemperature=0&amp;maxtemperature=1&amp;mintemperature=0&amp;mintemperature=1&amp;windspeed=0&amp;windspeed=1&amp;windgust=0&amp;windgust=1&amp;winddirection=0&amp;winddirection=1&amp;uv=0&amp;uv=1&amp;humidity=0&amp;precipitation=0&amp;precipitation=1&amp;precipitationprobability=0&amp;precipitationprobability=1&amp;spot=0&amp;pressure=0&amp;layout=light'
			},
			'hazards': {
				'M': {
					'environment': {
						'SS': ['Very shallow waters are found between and around the islands of Ufenau and Lützelau', 'Yellow buoys mark protected wildlife areas at several points along the coast. All paddle craft must stay outside the areas marked by these buoys']
					},
					'wildlife': {
						'SS': ['No wildlife hazards known']
					},
					'weather': {
						'SS': ['Swell and waves can form to the east of Hurden in northerly winds']
					},
					'traffic': {
						'SS': ['The canal at Pfäffikon is heavy trafficked by private boats when the weather is good. The narrow channel can amplify the effect of their wakes on paddle craft.', 'Swimmers from private boats are common between the islands of Ufenau and Lützelau']
					}
				}
			},
			'routeID': {
				'S': hashlib.sha1(routeName).hexdigest()[-8:]
			},
			'location': {
				'S': 'Obersee'
			},
			'urlMap': {
				'S': 'https://raw.githubusercontent.com/binghamchris/kayaklaun.ch/gh-pages/map/lachen.kml'
			},
			'descriptionShort': {
				'S': "An active day's paddling around the southern end of Lake Zürich, through the canals at Pfäffikon, and in between the islands of Ufenau and Lützelau."
			},
			'urlHeadlineImg': {
				'S': 'https://raw.githubusercontent.com/binghamchris/kayaklaun.ch/gh-pages/img/lachen-background.jpg'
			},
			'type': {
				'S': 'A-B'
			}
		}
	)
else:
	print "Please enter the DynamoDB table name as the first argument"