import React from 'react'
import { Icon, Label, Menu, Table, Grid, Responsive, Segment, Header} from 'semantic-ui-react'
import { HTTP } from 'meteor/http'


class Main extends React.Component{
  constructor(props){
      super(props);
      this.state={area:[]}
      try {
          var result= HTTP.get('http://localhost:2000/area?format=json', (err, resp)=>{
             this.setState({area: JSON.parse(resp.content)})
          })

      } catch (e) {
          console.log(e)
      }

  }

  render(){
      return(
        <Grid columns={3}>
            <Segment placeholder>
                <Grid.Column>
                    <Table celled>
                        <Table.Header>
                            <Table.Row>
                                <Table.HeaderCell>Commune</Table.HeaderCell>
                                <Table.HeaderCell>Cercle</Table.HeaderCell>
                            </Table.Row>
                        </Table.Header>
                        <Table.Body>
                            {
                                this.state.area.map((el, id)=>{
                                    return  <Table.Row key={id}>
                                                <Table.Cell>{el.name}</Table.Cell>
                                                <Table.Cell>{el.town}</Table.Cell>
                                            </Table.Row>
                                })
                            }
                        </Table.Body>
                    </Table>
                </Grid.Column>
            </Segment>
        </Grid>
      )
  }
}

export default Main
