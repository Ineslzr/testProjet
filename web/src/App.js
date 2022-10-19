import React, {useState, useEffect} from 'react';

function App(){

	const [data,setData] = useState([{}])
	useEffect(() => {
		fetch("/Users").then(
			res => res.json()
		).then(
			data => {
				setData(data)
				console.log(data)
			}
		)
	}, [])
	
	return(
		<div>
			{(typeof data === 'undefined') ? (
				<p>Loading...</p>
			) : (
				data.map((user,i) => (
					<p key={i}>{user}</p>
				))
			)}

		</div>
	)
  
}

export default App