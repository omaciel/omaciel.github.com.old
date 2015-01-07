Calling All Constructors
########################
:slug: calling-all-constructors
:date: 2005-03-30 19:07
:category:
:tags: english

I wanted to change some code I had written last week so that an
::google(“overloaded constructor”, “overloaded constructor”):: would
call the default constructor. This is usefull when you have to perform
an initialization to a class member no matter what constructor is called
during the class’ initialization. I faintly remembered Java’s Base and
SuperBase(?) syntax and tried several combinations of **this** and
**base** keywords. Nothing seemed to work… That’s when I came across
`this <http://weblogs.asp.net/acampbell/archive/2005/02/02/365299.aspx>`__
post which gave me the answer:

``  public class PostList     {``

::

        private ArrayList m_Posts;

        #region Constructor

        public PostList()
        {
            m_Posts = new ArrayList();
        }

        public PostList(XmlNode posts): this()
        {
            PopulatePosts(posts);
        }

        #endregion

}
