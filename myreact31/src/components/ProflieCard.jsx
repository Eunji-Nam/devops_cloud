import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faStickyNote,
  faEnvelope,
} from "@fortawesome/free-solid-svg-icons";
import { faFacebook, faInstagram } from "@fortawesome/free-brands-svg-icons";
import "./ProfileCard.css";

function ProfileCard({
  unique_id,
  name,
  role,
  mbti,
  instagram_url,
  profile_image_url,
  // profileImage,
  // name,
  // role,
  // facebookUrl,
  // email,
  children,
}) {
  return (
    <div>
      <h2>Profile Card</h2>
      <section>
        <nav className="menu">
          <a href="#">
            <FontAwesomeIcon icon={faBars} />
          </a>
          <a href="#">
            <FontAwesomeIcon icon={faStickyNote} />
          </a>
        </nav>
        <article className="profile">
          <img src={profile_image_url} />

          <h1>{name}</h1>
          <h2>{role}</h2>
          <h3>{mbti}</h3>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faInstagram} />
            <span>{instagram_url}</span>
          </li>
          {/* <li>
            <FontAwesomeIcon icon={faEnvelope} />
            <span>{email}</span>
          </li> */}
        </ul>
        <nav className="others">{children}</nav>
      </section>
    </div>
  );
}

export default ProfileCard;
