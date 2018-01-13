import React, { Component } from 'react';

export default class Search extends Component
{
    render() {
        return (
            <div>
                <input type="text" id="query"/>
                <button type="submit" onSubmit={this.props.onSubmit}>Submit</button>
            </div>
        );
    }
}