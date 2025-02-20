from django.shortcuts import render

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def about(request):
    
    """ A view to return the artist detail page """
    artist_description = """
        James Stanisław's artistic journey is an exploration of the unseen—the layers beneath the surface, both in the world around us and within ourselves. 
        Inspired by his father’s mastery of revealing the hidden beauty in wood and stone, James expanded this philosophy into his own evolving body of work, 
        capturing the depth of human experience, emotion, and motion through his art.

        Each piece in The Art Beneath collection is more than just a visual composition—it is a reflection of the moments that shaped him. His work shifts and transforms, 
        much like life itself, evolving with each stage of his journey. From his early years of boundless energy on the football field to the quiet introspection of adulthood, 
        his art tells the story of growth, struggle, triumph, and discovery.

        James' passion for football and movement often finds its way into his work, with bold strokes and dynamic textures mirroring the rhythm of the game. 
        The strength and precision required in both art and sport intertwine in his pieces, capturing the momentum of life itself. At the same time, his deep appreciation 
        for detail and hidden meaning, inherited from his father’s artistic philosophy, allows him to create works that invite viewers to look closer, to uncover layers 
        of emotion, memory, and personal evolution.

        Through The Art Beneath, James challenges us to see beyond the surface—to recognize that art, much like people, carries layers of history, passion, and meaning. 
        His work is not static; it breathes, shifts, and grows, just as he has. Each piece is a window into a moment in time, an invitation to explore not just what is seen, 
        but what lies beneath.
    """
    
    return render(request, 'home/about.html', {'artist_description': artist_description})
