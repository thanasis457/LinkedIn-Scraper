import "./App.css";
import {
  Button,
  ListItem as Item,
  Grid,
  InputBase,
  CircularProgress,
  Stack,
} from "@mui/material";
import { useRef, useState } from "react";
import getProfile from "./api/Profile";

function App() {
  const profileInput = useRef(null);
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(false);
  const handler = () => {
    setLoading(true);
    getProfile(profileInput.current.value)
      .then((res) => {
        setProfile(res.data);
        setError(false);
        setLoading(false);
      })
      .catch((e) => {
        console.log(e);
        setProfile("That through an error");
        setLoading(false);
        setError(true);
      });
  };
  return (
    <div className='App'>
      <header className='App-header'>
        <div className='title'>LinkedIn Profile Scraper</div>
        <Grid container spacing={1} style={{ width: "80%" }}>
          <Grid item xs={2}/>
          <Grid item xs={8}>
            <Item>
              <InputBase
                className='ProfileInput'
                placeholder='Type Profile URL to be scraped'
                inputRef={(r) => {
                  profileInput.current = r;
                }}
                onKeyDown={(event) => {
                  if (event.key === "Enter" && !loading) {
                    handler();
                  }
                }}
              />
            </Item>
          </Grid>
          <Grid item xs={2}>
            <Item>
              <Button variant='contained' onClick={handler} disabled={loading}>
                Scrape
              </Button>
            </Item>
          </Grid>
        </Grid>
        <Profile profile={profile} loading={loading} error={error} />
      </header>
    </div>
  );
}
function Profile({ profile = null, loading = false, error = false }) {
  console.log(profile);
  return loading ? (
    <CircularProgress />
  ) : error ? (
    <div>That threw an error!</div>
  ) : profile ? (
    <Stack
      style={{
        maxWidth: "80%",
        textAlign: "left",
        justifyContent: "flex-start",
      }}
    >
      <Item>Name: {profile.name}</Item>
      <Item>Title Description: {profile.titleDescription}</Item>
      <Item>Location: {profile.location}</Item>
      <Item>About: {profile.about}</Item>
      <Item>
        Experiences:
        <Stack style={{ maxHeight: "400px", overflow: "scroll" }}>
          {profile.experiences.map((item) => (
              <ul>
                <li>Position: {item.position}</li>
                <li>Company: {item.company}</li>
                <li>Date Range: {item.dateRange}</li>
                <li>Location: {item.location}</li>
                <li>Job Type: {item.type}</li>
                <li>Description: {item.description}</li>
              </ul>
            ))}
        </Stack>
      </Item>
      <Item>
        Education:
        <Stack style={{ maxHeight: "400px", overflow: "scroll" }}>
          {profile.education.map((item) => (
              <ul>
                <li>School: {item.name}</li>
                <li>Degree: {item.degree}</li>
                <li>Date Range: {item.dateRange}</li>
                <li>Description: {item.description}</li>
              </ul>
            ))}
        </Stack>
      </Item>
      <Item>
        Recommendations:
        <Stack style={{ maxHeight: "400px", overflow: "scroll" }}>
          {profile.recommendations.map((item) => (
              <ul>
                <li>Recommender: {item.name}</li>
                <li>
                  Profile: <a href={item.profile}>{item.profile}</a>
                </li>
                <li>Date of Testimonial: {item.date}</li>
                <li>Relationship: {item.relationship}</li>
                <li>Testimonial: {item.testimonial}</li>
              </ul>
            ))}
        </Stack>
      </Item>
    </Stack>
  ) : (
    <></>
  );
}

export default App;
