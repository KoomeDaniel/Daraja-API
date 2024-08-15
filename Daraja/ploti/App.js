import React, {Component} from 'react';
import {  Text, TouchableOpacity, View,Alert} from 'react-native';

class App extends Component {
  constructor(props){
    super(props)
  
  this.state = {
    value:0
  }
}
  add = () => {
    this.setState({value:this.state.value +1})
  };

  buttonClicked = () => {
    Alert.alert("I'm clicked")
  };
 
  render(){
  return (
    <View style={{flex:1,
      flexdirection:'column',
      justifyContent:'center',
      alignItems:'center',
    }}>{this.state.value >= 10?
      (<Text>You have reched level 10</Text>)
      : null
    }
    <View >
        <Text>{this.state.value}</Text>
        
        <TouchableOpacity onPress={this.buttonClicked}><Text>add</Text></TouchableOpacity>
        <TouchableOpacity onPress={this.add}><Text>add one</Text></TouchableOpacity>
    </View>
    </View>
  );
}
}

export default App;


