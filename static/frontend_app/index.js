import React from "react";
import ReactDOM from "react-dom";
import PropTypes from 'prop-types';
// import appbar from ./components/appbar;
// import footer from ./components/footer;

/*
You can write all your final renders in this script.
Write all the modular components in the COMPONENTS folder and import it here.
Here's a line to give you a headstart
*/


class FinalRender extends React.Component {
  render() {
    return (
			<div className="maindiv">
				<h1>This a frontend app based on Django and ReactJS</h1>
			</div>
    );
  }
}


ReactDOM.render(<FinalRender/>, document.getElementById('app'));
