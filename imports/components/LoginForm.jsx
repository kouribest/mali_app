import React from 'react'
import { Button, Form, Grid, Header, Image, Message, Segment } from 'semantic-ui-react'

class Login extends React.Component{
    constructor(props){
        super(props);

        this.state={
            email:'',
            password:''
        }

        this.updateField= this.updateField.bind(this)
    }

    updateField(event){
        console.log(event.target.id)
        var key=[]
        key[event.target.id]= event.target.value

        this.setState(key)
        console.log(this.state)
    }

    handleSubmit(event){
        console.log(this.state)
    }
  render(){
      return(
          <div className='login-form'>

            <style>{`
              body > div,
              body > div > div,
              body > div > div > div.login-form {
                height: 100%;
              }

            `}</style>
            <Grid textAlign='center' style={{ height: '100%' }} verticalAlign='middle'>
              <Grid.Column style={{ maxWidth: 650}}>
                <Header as='h2' color='black' textAlign='center'>
                    <Image src='/img/ps.png' /> Log-in to your account
                </Header>
                <Form size='large' onSubmit={this.handleSubmit}>
                  <Segment stacked>
                    <Form.Input
                        id='email'
                        fluid
                        icon='user'
                        iconPosition='left'
                        placeholder='E-mail address'
                        onChange={this.updateField}

                    />
                    <Form.Input
                        fluid
                        id='password'
                        icon='lock'
                        iconPosition='left'
                        placeholder='Password'
                        type='password'
                        onChange={this.updateField}

                    />

                <Button onClick={this.updateField} color='black' fluid size='large'>
                      Login
                    </Button>
                  </Segment>
                </Form>
                <Message>
                 Need an admin account? Contact <a href='mailto:skouriba@outlook.fr'>KOURIBA Soumaila</a>
                </Message>
              </Grid.Column>
            </Grid>
          </div>
      )
  }
}

export default Login
