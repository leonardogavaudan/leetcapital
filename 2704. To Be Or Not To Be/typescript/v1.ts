type ToBeOrNotToBe = {
	toBe: (val: any) => boolean;
	notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
	return {
		toBe: (x) => {
			if (val !== x) {
				throw new Error("Not Equal");
			}
			return true;
		},
		notToBe: (x) => {
			if (val === x) {
				throw new Error("Equal");
			}
			return true;
		},
	};
}
