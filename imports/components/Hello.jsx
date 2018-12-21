import React, { Component } from 'react';
import PropTypes from 'prop-types'
import { Button, Header, Icon, Segment } from 'semantic-ui-react'
import {SegmentExemple} from './Exemple'

export default class Hello extends Component {
  state = {
    counter: 0,
  }

  increment() {
    this.setState({
      counter: this.state.counter + 1
    });
  }

  render() {
    return (
      <div>
        <button onClick={() => this.increment()}>Click Me</button>
        <p>You've pressed the button {this.state.counter} times.</p>
      </div>

    );
  }
}
