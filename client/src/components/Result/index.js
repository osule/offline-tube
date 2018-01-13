import React, { Component } from 'react';

export default class Result extends Component
{
    render() {
        const {results} = this.props;
        if (results) {
            
            return this.results.formats.map((file) => (
                <div>
                    {file.format} - {file.filesize}
                    <a href="{file.url}" download>Download</a>
                </div>
            ));
        }
        return results;
    }
}