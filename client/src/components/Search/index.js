import React, { Component } from 'react';
import './Search.css';

export default class Search extends Component
{
    render() {
        return (
            <div className="Search-container">
                <input className="Search-input" type="text" id="query"/>
                <button className="Search-button" type="submit" onSubmit={this.props.onSubmit}>Submit</button>
            </div>
        );
    }
}