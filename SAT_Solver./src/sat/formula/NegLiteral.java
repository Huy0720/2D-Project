package sat.formula;
import sat.env.Bool;
import sat.env.Environment;
import sat.env.Variable;

/**
 * Class representing negative literals.
 * Works with PosLiteral to ensure interning of literals.
 * NegLiteral objects are immutable.
 */
public class NegLiteral extends Literal {

    // should NOT be used by clients
    NegLiteral(String name) {
        super(name);
    }

    public static NegLiteral make (Variable var) {
        return make(var.getName());
    }
    
    public static NegLiteral make (String name) {
        Literal posLiteral = PosLiteral.make(name);
        return (NegLiteral) posLiteral.getNegation();
    }

    public Bool eval (Environment e) {
        return e.get(this.var).not();
    }

    public String toString() {
        return "~" + var;
    }

}
