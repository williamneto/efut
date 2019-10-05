import React from "react"

export default props => {
    return (
        <div className="rank">
            <ul className="rank-ul">
                {props.rank.map(user => (
                    <li> {user.username} {user.points}</li>
                ))}
            </ul>
        </div>
    )
}