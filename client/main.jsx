import React from 'react';
import { Meteor } from 'meteor/meteor';
import { render } from 'react-dom';
import Login from '/imports/components/LoginForm'
import Main from '/imports/components/main'
import FixedMenuLayout from '/imports/components/MainContainer'

Meteor.startup(() => {
  render(<FixedMenuLayout />, document.getElementById('react-target'));
});
