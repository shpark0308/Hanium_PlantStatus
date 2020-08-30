import React, {Component} from 'react';
import { WebView } from 'react-native-webview';

export default class YourApp extends Component<{}> { 
  render() {
    return (
      <WebView
        //source={{uri: 'https://github.com/facebook/react-native'}}
        source={{uri: 'http://127.0.0.1:8000/'}}
        style={{marginTop: 20}}
      />
    );
  }
}