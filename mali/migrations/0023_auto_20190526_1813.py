# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-26 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mali', '0022_auto_20190518_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malimodel',
            name='allant_a',
            field=models.CharField(choices=[('Bangladesh', 'Bangladesh'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Burkina Faso', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Barbados', 'Barbados'), ('Belgium', 'Belgium'), ('Saint Barthelemy', 'Saint Barthelemy'), ('Bermuda', 'Bermuda'), ('Brunei', 'Brunei'), ('Bolivia', 'Bolivia'), ('Japan', 'Japan'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Jamaica', 'Jamaica'), ('Bouvet Island', 'Bouvet Island'), ('Jordan', 'Jordan'), ('Samoa', 'Samoa'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Brazil', 'Brazil'), ('Bahamas', 'Bahamas'), ('Jersey', 'Jersey'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Serbia', 'Serbia'), ('Lithuania', 'Lithuania'), ('Reunion', 'Reunion'), ('Luxembourg', 'Luxembourg'), ('Liberia', 'Liberia'), ('Romania', 'Romania'), ('Lesotho', 'Lesotho'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Greece', 'Greece'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Bahrain', 'Bahrain'), ('Guyana', 'Guyana'), ('Guernsey', 'Guernsey'), ('French Guiana', 'French Guiana'), ('Georgia', 'Georgia'), ('Grenada', 'Grenada'), ('United Kingdom', 'United Kingdom'), ('Gabon', 'Gabon'), ('El Salvador', 'El Salvador'), ('Guinea', 'Guinea'), ('Gambia', 'Gambia'), ('Greenland', 'Greenland'), ('Gibraltar', 'Gibraltar'), ('Ghana', 'Ghana'), ('Oman', 'Oman'), ('Israel', 'Israel'), ('Botswana', 'Botswana'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Hong Kong', 'Hong Kong'), ('Honduras', 'Honduras'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Venezuela', 'Venezuela'), ('Puerto Rico', 'Puerto Rico'), ('Palestine, State of', 'Palestine, State of'), ('Palau', 'Palau'), ('Portugal', 'Portugal'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Paraguay', 'Paraguay'), ('Iraq', 'Iraq'), ('Panama', 'Panama'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Peru', 'Peru'), ('Pakistan', 'Pakistan'), ('Philippines', 'Philippines'), ('Pitcairn', 'Pitcairn'), ('Poland', 'Poland'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Zambia', 'Zambia'), ('Western Sahara', 'Western Sahara'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('South Africa', 'South Africa'), ('Ecuador', 'Ecuador'), ('Italy', 'Italy'), ('Vietnam', 'Vietnam'), ('Solomon Islands', 'Solomon Islands'), ('Ethiopia', 'Ethiopia'), ('Somalia', 'Somalia'), ('Zimbabwe', 'Zimbabwe'), ('Saudi Arabia', 'Saudi Arabia'), ('Spain', 'Spain'), ('Eritrea', 'Eritrea'), ('Montenegro', 'Montenegro'), ('Moldova', 'Moldova'), ('Madagascar', 'Madagascar'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Uzbekistan', 'Uzbekistan'), ('Myanmar', 'Myanmar'), ('Mali', 'Mali'), ('Macao', 'Macao'), ('Mongolia', 'Mongolia'), ('Marshall Islands', 'Marshall Islands'), ('Macedonia', 'Macedonia'), ('Mauritius', 'Mauritius'), ('Malta', 'Malta'), ('Malawi', 'Malawi'), ('Maldives', 'Maldives'), ('Martinique', 'Martinique'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Montserrat', 'Montserrat'), ('Mauritania', 'Mauritania'), ('Isle of Man', 'Isle of Man'), ('Uganda', 'Uganda'), ('Malaysia', 'Malaysia'), ('Mexico', 'Mexico'), ('Mozambique', 'Mozambique'), ('France', 'France'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands  [Malvinas]', 'Falkland Islands  [Malvinas]'), ('Micronesia (Federated States of)', 'Micronesia (Federated States of)'), ('Faroe Islands', 'Faroe Islands'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Middle Earth', 'Middle Earth'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('Cook Islands', 'Cook Islands'), ('Ivory Cost', 'Ivory Cost'), ('Switzerland', 'Switzerland'), ('Colombia', 'Colombia'), ('China', 'China'), ('Cameroon', 'Cameroon'), ('Chile', 'Chile'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Canada', 'Canada'), ('Congo', 'Congo'), ('Central African Republic', 'Central African Republic'), ('Congo (the Democratic Republic of the)', 'Congo (the Democratic Republic of the)'), ('Czechia', 'Czechia'), ('Cyprus', 'Cyprus'), ('Christmas Island', 'Christmas Island'), ('Costa Rica', 'Costa Rica'), ('Cabo Verde', 'Cabo Verde'), ('Cuba', 'Cuba'), ('Swaziland', 'Swaziland'), ('Syria', 'Syria'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Kenya', 'Kenya'), ('South Sudan', 'South Sudan'), ('Suriname', 'Suriname'), ('Kiribati', 'Kiribati'), ('Cambodia', 'Cambodia'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Comoros', 'Comoros'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Slovakia', 'Slovakia'), ('South Korea', 'South Korea'), ('Slovenia', 'Slovenia'), ('North Korea', 'North Korea'), ('Kuwait', 'Kuwait'), ('Senegal', 'Senegal'), ('San Marino', 'San Marino'), ('Sierra Leone', 'Sierra Leone'), ('Seychelles', 'Seychelles'), ('Kazakhstan', 'Kazakhstan'), ('Cayman Islands', 'Cayman Islands'), ('Singapore', 'Singapore'), ('Sweden', 'Sweden'), ('Sudan', 'Sudan'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Virgin Islands (British)', 'Virgin Islands (British)'), ('Germany', 'Germany'), ('Yemen', 'Yemen'), ('Austria', 'Austria'), ('Algeria', 'Algeria'), ('United States of America', 'United States of America'), ('Latvia', 'Latvia'), ('Uruguay', 'Uruguay'), ('Mayotte', 'Mayotte'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Lebanon', 'Lebanon'), ('Saint Lucia', 'Saint Lucia'), ('Laos', 'Laos'), ('Tuvalu', 'Tuvalu'), ('Taiwan', 'Taiwan'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Turkey', 'Turkey'), ('Sri Lanka', 'Sri Lanka'), ('Liechtenstein', 'Liechtenstein'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('Timor-Leste', 'Timor-Leste'), ('Turkmenistan', 'Turkmenistan'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Thailand', 'Thailand'), ('French Southern Territories', 'French Southern Territories'), ('Togo', 'Togo'), ('Chad', 'Chad'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Libya', 'Libya'), ('Holy See', 'Holy See'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('United Arab Emirates', 'United Arab Emirates'), ('Andorra', 'Andorra'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Afghanistan', 'Afghanistan'), ('Anguilla', 'Anguilla'), ('Virgin Islands (U.S.)', 'Virgin Islands (U.S.)'), ('Iceland', 'Iceland'), ('Iran', 'Iran'), ('Armenia', 'Armenia'), ('Albania', 'Albania'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('American Samoa', 'American Samoa'), ('Argentina', 'Argentina'), ('Australia', 'Australia'), ('Vanuatu', 'Vanuatu'), ('Aruba', 'Aruba'), ('India', 'India'), ('Tanzania', 'Tanzania'), ('Azerbaijan', 'Azerbaijan'), ('Ireland', 'Ireland'), ('Indonesia', 'Indonesia'), ('Ukraine', 'Ukraine'), ('Qatar', 'Qatar')], max_length=50, verbose_name='Destination'),
        ),
        migrations.AlterField(
            model_name='malimodel',
            name='venant_de',
            field=models.CharField(choices=[('Bangladesh', 'Bangladesh'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Burkina Faso', 'Burkina Faso'), ('Bulgaria', 'Bulgaria'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Barbados', 'Barbados'), ('Belgium', 'Belgium'), ('Saint Barthelemy', 'Saint Barthelemy'), ('Bermuda', 'Bermuda'), ('Brunei', 'Brunei'), ('Bolivia', 'Bolivia'), ('Japan', 'Japan'), ('Burundi', 'Burundi'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Jamaica', 'Jamaica'), ('Bouvet Island', 'Bouvet Island'), ('Jordan', 'Jordan'), ('Samoa', 'Samoa'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Brazil', 'Brazil'), ('Bahamas', 'Bahamas'), ('Jersey', 'Jersey'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Serbia', 'Serbia'), ('Lithuania', 'Lithuania'), ('Reunion', 'Reunion'), ('Luxembourg', 'Luxembourg'), ('Liberia', 'Liberia'), ('Romania', 'Romania'), ('Lesotho', 'Lesotho'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Greece', 'Greece'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Bahrain', 'Bahrain'), ('Guyana', 'Guyana'), ('Guernsey', 'Guernsey'), ('French Guiana', 'French Guiana'), ('Georgia', 'Georgia'), ('Grenada', 'Grenada'), ('United Kingdom', 'United Kingdom'), ('Gabon', 'Gabon'), ('El Salvador', 'El Salvador'), ('Guinea', 'Guinea'), ('Gambia', 'Gambia'), ('Greenland', 'Greenland'), ('Gibraltar', 'Gibraltar'), ('Ghana', 'Ghana'), ('Oman', 'Oman'), ('Israel', 'Israel'), ('Botswana', 'Botswana'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Hong Kong', 'Hong Kong'), ('Honduras', 'Honduras'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Venezuela', 'Venezuela'), ('Puerto Rico', 'Puerto Rico'), ('Palestine, State of', 'Palestine, State of'), ('Palau', 'Palau'), ('Portugal', 'Portugal'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Paraguay', 'Paraguay'), ('Iraq', 'Iraq'), ('Panama', 'Panama'), ('French Polynesia', 'French Polynesia'), ('Papua New Guinea', 'Papua New Guinea'), ('Peru', 'Peru'), ('Pakistan', 'Pakistan'), ('Philippines', 'Philippines'), ('Pitcairn', 'Pitcairn'), ('Poland', 'Poland'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Zambia', 'Zambia'), ('Western Sahara', 'Western Sahara'), ('Estonia', 'Estonia'), ('Egypt', 'Egypt'), ('South Africa', 'South Africa'), ('Ecuador', 'Ecuador'), ('Italy', 'Italy'), ('Vietnam', 'Vietnam'), ('Solomon Islands', 'Solomon Islands'), ('Ethiopia', 'Ethiopia'), ('Somalia', 'Somalia'), ('Zimbabwe', 'Zimbabwe'), ('Saudi Arabia', 'Saudi Arabia'), ('Spain', 'Spain'), ('Eritrea', 'Eritrea'), ('Montenegro', 'Montenegro'), ('Moldova', 'Moldova'), ('Madagascar', 'Madagascar'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Uzbekistan', 'Uzbekistan'), ('Myanmar', 'Myanmar'), ('Mali', 'Mali'), ('Macao', 'Macao'), ('Mongolia', 'Mongolia'), ('Marshall Islands', 'Marshall Islands'), ('Macedonia', 'Macedonia'), ('Mauritius', 'Mauritius'), ('Malta', 'Malta'), ('Malawi', 'Malawi'), ('Maldives', 'Maldives'), ('Martinique', 'Martinique'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Montserrat', 'Montserrat'), ('Mauritania', 'Mauritania'), ('Isle of Man', 'Isle of Man'), ('Uganda', 'Uganda'), ('Malaysia', 'Malaysia'), ('Mexico', 'Mexico'), ('Mozambique', 'Mozambique'), ('France', 'France'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands  [Malvinas]', 'Falkland Islands  [Malvinas]'), ('Micronesia (Federated States of)', 'Micronesia (Federated States of)'), ('Faroe Islands', 'Faroe Islands'), ('Nicaragua', 'Nicaragua'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Middle Earth', 'Middle Earth'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('Niue', 'Niue'), ('Cook Islands', 'Cook Islands'), ('Ivory Cost', 'Ivory Cost'), ('Switzerland', 'Switzerland'), ('Colombia', 'Colombia'), ('China', 'China'), ('Cameroon', 'Cameroon'), ('Chile', 'Chile'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Canada', 'Canada'), ('Congo', 'Congo'), ('Central African Republic', 'Central African Republic'), ('Congo (the Democratic Republic of the)', 'Congo (the Democratic Republic of the)'), ('Czechia', 'Czechia'), ('Cyprus', 'Cyprus'), ('Christmas Island', 'Christmas Island'), ('Costa Rica', 'Costa Rica'), ('Cabo Verde', 'Cabo Verde'), ('Cuba', 'Cuba'), ('Swaziland', 'Swaziland'), ('Syria', 'Syria'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Kenya', 'Kenya'), ('South Sudan', 'South Sudan'), ('Suriname', 'Suriname'), ('Kiribati', 'Kiribati'), ('Cambodia', 'Cambodia'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Comoros', 'Comoros'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Slovakia', 'Slovakia'), ('South Korea', 'South Korea'), ('Slovenia', 'Slovenia'), ('North Korea', 'North Korea'), ('Kuwait', 'Kuwait'), ('Senegal', 'Senegal'), ('San Marino', 'San Marino'), ('Sierra Leone', 'Sierra Leone'), ('Seychelles', 'Seychelles'), ('Kazakhstan', 'Kazakhstan'), ('Cayman Islands', 'Cayman Islands'), ('Singapore', 'Singapore'), ('Sweden', 'Sweden'), ('Sudan', 'Sudan'), ('Dominican Republic', 'Dominican Republic'), ('Dominica', 'Dominica'), ('Djibouti', 'Djibouti'), ('Denmark', 'Denmark'), ('Virgin Islands (British)', 'Virgin Islands (British)'), ('Germany', 'Germany'), ('Yemen', 'Yemen'), ('Austria', 'Austria'), ('Algeria', 'Algeria'), ('United States of America', 'United States of America'), ('Latvia', 'Latvia'), ('Uruguay', 'Uruguay'), ('Mayotte', 'Mayotte'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Lebanon', 'Lebanon'), ('Saint Lucia', 'Saint Lucia'), ('Laos', 'Laos'), ('Tuvalu', 'Tuvalu'), ('Taiwan', 'Taiwan'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Turkey', 'Turkey'), ('Sri Lanka', 'Sri Lanka'), ('Liechtenstein', 'Liechtenstein'), ('Tunisia', 'Tunisia'), ('Tonga', 'Tonga'), ('Timor-Leste', 'Timor-Leste'), ('Turkmenistan', 'Turkmenistan'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Thailand', 'Thailand'), ('French Southern Territories', 'French Southern Territories'), ('Togo', 'Togo'), ('Chad', 'Chad'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Libya', 'Libya'), ('Holy See', 'Holy See'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('United Arab Emirates', 'United Arab Emirates'), ('Andorra', 'Andorra'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Afghanistan', 'Afghanistan'), ('Anguilla', 'Anguilla'), ('Virgin Islands (U.S.)', 'Virgin Islands (U.S.)'), ('Iceland', 'Iceland'), ('Iran', 'Iran'), ('Armenia', 'Armenia'), ('Albania', 'Albania'), ('Angola', 'Angola'), ('Antarctica', 'Antarctica'), ('American Samoa', 'American Samoa'), ('Argentina', 'Argentina'), ('Australia', 'Australia'), ('Vanuatu', 'Vanuatu'), ('Aruba', 'Aruba'), ('India', 'India'), ('Tanzania', 'Tanzania'), ('Azerbaijan', 'Azerbaijan'), ('Ireland', 'Ireland'), ('Indonesia', 'Indonesia'), ('Ukraine', 'Ukraine'), ('Qatar', 'Qatar')], max_length=50, verbose_name='Depart'),
        ),
    ]
